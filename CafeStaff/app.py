from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from BCE import *
from CafeDB import *
from forms import StaffSlotForm
import secrets

from flask import render_template, request

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    app.add_url_rule('/', view_func=BidsBoundary.render_all_bids)
    
    @app.route("/owner")
    def staff():
        work_slots = WorkSlot.query.all()
        return render_template('owner.html', work_slots=work_slots)
    
    @app.route("/staffbids")
    def staff_bids():
        bids = Bids.query.all()
        return render_template('staff_bids.html', bids=bids)
    
    @app.route("/create_room", methods=['GET', 'POST'])
    def create_slot():
        data = request.get_json()  # Get JSON data from the request

        # Extract data from the JSON object
        shift_type = data.get('shift_type')
        date = data.get('date')
        starttime = data.get('starttime')
        endtime = data.get('endtime')
        print(date)
        # Create a new WorkSlot instance
        new_slot = WorkSlot(shiftType=shift_type, date=date, status='AVAILABLE')

        try:
            # Add the new slot to the database and commit the transaction
            db.session.add(new_slot)
            db.session.commit()
            response = jsonify({"message": "Slot created successfully"}), 201

            # Optionally, return a success message as JSON response
            return response

        except Exception as e:
            # Handle any exceptions (e.g., database errors) and return an error message
            db.session.rollback()
            print(e)
            response = jsonify({"error": str(e)}), 500
            return response
    
    @app.route("/success")
    def success():
        return render_template('success.html')
        
        
    with app.app_context():
        db.drop_all()
        db.create_all()
        existing_role = UserRole.query.filter_by(role="CafeStaff").first()
        new_workslot = WorkSlot(
            shiftType = 'AFTERNOON',
            date = '01-01-2000',
            status = 'Available',
        )

        if existing_role:
            # Use the existing role
            new_user = Staff(
                username="John",
                password="John2",
                job="Waiter",
                avail="FT",
                userRole=existing_role.role,  # Use the existing role here
            )
        else:
            # Create a new role if it doesn't exist
            new_role = UserRole(role="CafeStaff")
            db.session.add(new_role)
            db.session.commit()

            # Use the newly created role
            new_user = Staff(
                username="John",
                password="John2",
                job="Waiter",
                avail="FT",
                userRole=new_role.role,
            )

        new_bid = Bids(
            shift_id = 1,
            shift_type = new_workslot.shiftType,
            shift_date = new_workslot.date,
            staff_user = new_user.username,
            approval = True,

        )
        
        db.session.add(new_workslot)
        db.session.add(new_role)
        db.session.add(new_user)
        db.session.add(new_bid)
        
        db.session.commit()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
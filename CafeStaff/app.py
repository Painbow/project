from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from BCE import *
from CafeDB import *

from flask import render_template, request

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///database.db"
    db.init_app(app)

    app.add_url_rule('/', view_func=BidsBoundary.render_all_bids)

    with app.app_context():
        db.drop_all()
        db.create_all()
        new_workslot = WorkSlot(
            id = 1,
            shiftType = 'AFTERNOON',
            date = '01-01-2000',
            status = 'Available',

        )

        new_role = UserRole(
            role = "CafeStaff",
        )

        new_user = Staff(
            username = "John",
            password = "John2",
            job = "Waiter",
            avail = "FT",
            userRole = new_role.role,
        )

        new_bid = Bids(
            id = 1,
            shift_id = new_workslot.id,
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

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

















from flask import render_template, request
from CafeDB import *

class WorkSlotBoundary:
    @staticmethod
    def render_available_work_slots():
        available_slots = WorkSlotController.get_from_entity()
        return render_template('available_slots.html', slots=available_slots)

    # Add methods to handle other views and user interactions

class BidsBoundary:
    @staticmethod
    def render_all_bids():
        all_bids = BidsController.get_from_entity_bids()
        return render_template('staff_bids.html', bids=all_bids)
    


class WorkSlotController:
    @staticmethod
    def get_from_entity():
        return WorkSlotEntity.get_available_work_slots()

    # Add methods to create, update, and delete work slots

class BidsController:
    @staticmethod
    def get_from_entity_bids():
        return BidsEntity.get_all_bids()
    
class WorkSlotEntity:
    @staticmethod
    def get_available_work_slots():
        return WorkSlot.query.filter_by(status='Available').all()

    # Add methods to create, update, and delete work slots 

class BidsEntity:
    @staticmethod
    def get_all_bids():
        return Bids.query.filter_by(staff_user = 'John').all()
    

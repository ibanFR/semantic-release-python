from lift_button.lift import Lift

# TEST LIST
# [] - doors should be CLOSED when Lift is created
# [] - should switch lights ON when button is pressed and doors are CLOSED
# [] - should OPEN the lift doors when lift arrives
# [] - should switch OFF the lights when lift arrives
# [] - lights should be OFF when button is pressed and doors are OPEN

def test_should_create_new_lift():
    lift = Lift()
    assert isinstance(lift, Lift)

def test_doors_should_be_closed_when_lift_is_created():
    lift = Lift()
    assert lift.doors == "CLOSED"
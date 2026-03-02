from sqlalchemy.orm import Session
from models import IceCream
from schemas import IceCreamCreate

# 1️⃣ Get all ice creams
def get_icecreams(db: Session):
    return db.query(IceCream).all()

# 2️⃣ Create a new ice cream
def create_icecream(db: Session, icecream: IceCreamCreate):
    db_icecream = IceCream(
        name=icecream.name,
        flavor=icecream.flavor,
        price=icecream.price,
        stock=icecream.stock
    )
    db.add(db_icecream)
    db.commit()
    db.refresh(db_icecream)
    return db_icecream

def update_icecream(db, icecream_id: int, icecream_data):
    icecream = db.query(IceCream).filter(IceCream.id == icecream_id).first()

    if not icecream:
        return None

    icecream.name = icecream_data.name
    icecream.flavor = icecream_data.flavor
    icecream.price = icecream_data.price
    icecream.stock = icecream_data.stock

    db.commit()
    db.refresh(icecream)

    return icecream
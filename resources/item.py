import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items
from schemas import ItemSchema, ItemUpdateSchema

item_blp = Blueprint("items", __name__, description="Operations on items")


@item_blp.route("/item/<string:item_id>")
class Item(MethodView): 
    @item_blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")
    
    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    @item_blp.arguments(ItemUpdateSchema)
    @item_blp.response(200, ItemSchema)
    def put(self, item_id, item_data):
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="Item not found.")

@item_blp.route("/item")
class ItemList(MethodView):
    @item_blp.response(200, ItemSchema(many=True))  
    def get(self):
        return items.values()
    
    @item_blp.arguments(ItemSchema)
    @item_blp.response(201, ItemSchema)
    def post(self, item_data):
        for item in items.values():
            if item_data["name"] == item["name"]:
                abort(400, message="Item already exists.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id]= item

        return item
    
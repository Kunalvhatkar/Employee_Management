from flask import Blueprint,request,jsonify,current_app
from bson import ObjectId
from utils.auth import token_required

employee_routes=Blueprint("employee",__name__)

@employee_routes.route("/employees",methods=["GET"])
@token_required
def get_employees():

    db=current_app.config["db"]

    employees=[]

    for emp in db.employees.find():

        emp["_id"]=str(emp["_id"])

        employees.append(emp)

    return jsonify(employees)


@employee_routes.route("/employees",methods=["POST"])
@token_required
def add_employee():

    db=current_app.config["db"]

    data=request.json

    db.employees.insert_one(data)

    return jsonify({"message":"Employee Added"})


@employee_routes.route("/employees/<id>",methods=["DELETE"])
@token_required
def delete_employee(id):

    db=current_app.config["db"]

    db.employees.delete_one({"_id":ObjectId(id)})

    return jsonify({"message":"Employee Deleted"})


@employee_routes.route("/employees/<id>",methods=["PUT"])
@token_required
def update_employee(id):

    db=current_app.config["db"]

    data=request.json

    db.employees.update_one(

        {"_id":ObjectId(id)},

        {

            "$set":data

        }

    )

    return jsonify({"message":"Employee Updated"})
from flask import Blueprint, jsonify, request, abort, Response
from datetime import datetime, timedelta
from supabase_client import Client



REQUEST_API = Blueprint('request_api', __name__)

url= 'https://tlagwlowvabyydvzipai.supabase.co'
key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRsYWd3bG93dmFieXlkdnppcGFpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NDY3NjY2MDksImV4cCI6MTk2MjM0MjYwOX0.jicG5Cyvw7wW7Sw_lkHQVqv6cEogH0YJzR_GrL7HEXM'
supabase = Client( 
	api_url=url,
	api_key=key
)




def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API




@REQUEST_API.route('/orders', methods=['GET', 'POST'])
async def get_records():
    if request.method == 'GET':
        error, result = await(supabase.table("order").limit(30).select("*").query())
        return jsonify(result)
    else:
        error, result = await(supabase.table("order").insert([request.get_json()]))
        return jsonify(result)


@REQUEST_API.route('/orders/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
async def handle_order(id):
    if request.method == "GET":
        error, data = await supabase.table("order").select("*").eq('id',id).query()
        if(error):
            data=error
        return jsonify(data)
    elif request.method == "PUT":
        return "ok"
    elif request.method == "DELETE":
        error, data = await supabase.table("order").delete({'id':id})
        
        return jsonify(data)
    else:
        return "not ok"
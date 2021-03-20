from api.utils.db_init import db


def get_rating(courier_id):
    sql_request = f"select min(x.avg) as min_rating from (select avg(difference_time) as avg, region from Orders where courier_id = {courier_id} and difference_time is not Null group by region)x limit 1;"
    result = db.engine.execute(sql_request)
    min_rating = result.fetchone()['min_rating']
    rating_courier = (60 * 60 - min(min_rating, 60 * 60)) / (60 * 60) * 5
    return round(rating_courier, 2)
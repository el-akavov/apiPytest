from requests import Response

from utils.api import Google_maps_api

# Создание, изменение, удадение новой локации
class Test_create_place():

    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Метод GET POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)

        print("Метод PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id)

        print("Метод GET PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)

        print("Метод DELETE")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)

        print("Метод GET DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id)
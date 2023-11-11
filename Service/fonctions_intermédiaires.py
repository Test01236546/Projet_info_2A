import time


#Regarder la complexité de ces deux fonctions

def no_print_map(map_ex):
        result = list(map_ex)
    
# no_print_map(map_ex)

def no_print_map2(map_ex):
        result = map_ex
        for _ in result:
            pass  # Ne rien faire dans la boucle

def periodic(Instance_service,duration, pause):
    start_time = time.time()
    while time.time() - start_time < duration:
        Instance_service.ingest()
        time.sleep(pause)


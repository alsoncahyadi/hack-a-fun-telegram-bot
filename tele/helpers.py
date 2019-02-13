from django.http import HttpResponse, JsonResponse
import random, os, json, traceback

def generate_salt(n=16):
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars=[]
    for i in range(n):
        chars.append(random.choice(ALPHABET))

    
    return "".join(chars)

def is_message_valid(req_json):
    try:
        if req_json['message']['from']['is_bot']:
            return False
        req_json['message']['text']
    except:
        return False

    return True

def get_log(request):
    def get_object_log_str(obj):
        if obj.__class__ == ''.__class__:
            return "'" + str(obj) + "'"
        else:
            return str(obj)

    log_entries = {
        'agent': request.META.get('HTTP_USER_AGENT', ''),
        'remote_host': ' | '.join([request.META.get('REMOTE_ADDR'), request.META.get('HTTP_ORIGIN', '')]),
        'data': request.data,
    }
    log_entries_list = ["'{k}': {v}".format(k=k, v=get_object_log_str(v)) for k, v in log_entries.items()]
    return "{ " + "; ".join(log_entries_list) + " }"

def error_response(code, message):
    message_entry = {
        'code': code,
        'message': message,
        'stack_trace': traceback.format_exc(5).splitlines(),
    }
    print(message_entry)
    return JsonResponse(message_entry, status=code)

def game_type_to_i(game_type_s):
    return {
        'ctr_tournament': 2,
        'ctr_free_play': 3,
        'cerdas_cermat': 4,
        'ranking_1': 5,
        'guitar_hero': 6,
        'cs_go': 7,
        'winning_eleven': 8,
        'baby_rattle': 9,
        'move_up_cup': 10,
        'jumping_the_riddles': 11,
        'inferno_extinguisher': 12,
        'floating_ball_race': 13,
        'human_table_soccer': 14,
    }.get(game_type_s, None)

def game_type_to_s(game_type_i):
    return {
        2: 'ctr_tournament',
        3: 'ctr_free_play',
        4: 'cerdas_cermat',
        5: 'ranking_1',
        6: 'guitar_hero',
        7: 'cs_go',
        8: 'winning_eleven',
        9: 'baby_rattle',
        10: 'move_up_cup',
        11: 'jumping_the_riddles',
        12: 'inferno_extinguisher',
        13: 'floating_ball_race',
        14: 'human_table_soccer',
    }.get(game_type_i, None)

def game_type_s_to_name(game_type_s):
    return {
        'ctr_tournament': 'CTR Tournament',
        'ctr_free_play': 'CTR Free Play',
        'cerdas_cermat': 'Cerdas Cermat',
        'ranking_1': 'Ranking 1',
        'guitar_hero': 'Guitar Hero',
        'cs_go': 'Counter Strike: Global Offensive',
        'winning_eleven': 'Winning Eleven',
        'baby_rattle': 'Baby Rattle',
        'move_up_cup': 'Move Up Cup',
        'jumping_the_riddles': 'Jumping The Riddles',
        'inferno_extinguisher': 'Inferno Extinguisher',
        'floating_ball_race': 'Floating Ball Race',
        'human_table_soccer': 'Human Table Soccer',
    }.get(game_type_s, None)

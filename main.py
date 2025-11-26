import sys
from opcua import ua, Server
from random import randint, choice, uniform

server = Server()
# Можно указать IP-адрес нужного интерфейса
server.set_endpoint("opc.tcp://0.0.0.0:4840/")
server.set_server_name("Server")

# Пространство имен
uri = "http://server"
idx = server.register_namespace(uri)
objects = server.get_objects_node()

# Словарь объектов и их переменных
obj_dict = [{
    'Input_AI_DB': [{'AI_FlowSlurry':[
                                    ['Raw', 'int16'],
                                    ['EU_Raw_Min', 'float'],
                                    ['EU_Raw_Max', 'float'],
                                    ['HH_En', 'bool'],
                                    ['H_En', 'bool'],
                                    ['L_En', 'bool'],
                                    ['LL_En', 'bool'],
                                    ['CH_OFF', 'bool'],
                                    ['EU_SUBST', 'float'],
                                    ['HH_Limit', 'float'],
                                    ['H_Limit', 'float'],
                                    ['L_Limit', 'float'],
                                    ['LL_Limit', 'float'],
                                    ['Hyst', 'float'],
                                    {'HMI.Status': [
                                        ['PV', 'float'],
                                        ['SF', 'bool'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ]
                                     }
                                    ]
                    },

                    {'AI_PressSlurry':[
                                        ['Raw', 'int16'],
                                        ['EU_Raw_Min', 'float'],
                                        ['EU_Raw_Max', 'float'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ['CH_OFF', 'bool'],
                                        ['EU_SUBST', 'float'],
                                        ['HH_Limit', 'float'],
                                        ['H_Limit', 'float'],
                                        ['L_Limit', 'float'],
                                        ['LL_Limit', 'float'],
                                        ['Hyst', 'float'],
                                        {'HMI.Status': [
                                            ['PV', 'float'],
                                            ['SF', 'bool'],
                                            ['HH_En', 'bool'],
                                            ['H_En', 'bool'],
                                            ['L_En', 'bool'],
                                            ['LL_En', 'bool'],
                                            ]
                                        }
                                        ]
                    },

                    {'AI_FlowWiring':[
                                        ['Raw', 'int16'],
                                        ['EU_Raw_Min', 'float'],
                                        ['EU_Raw_Max', 'float'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ['CH_OFF', 'bool'],
                                        ['EU_SUBST', 'float'],
                                        ['HH_Limit', 'float'],
                                        ['H_Limit', 'float'],
                                        ['L_Limit', 'float'],
                                        ['LL_Limit', 'float'],
                                        ['Hyst', 'float'],
                                        {'HMI.Status': [
                                            ['PV', 'float'],
                                            ['SF', 'bool'],
                                            ['HH_En', 'bool'],
                                            ['H_En', 'bool'],
                                            ['L_En', 'bool'],
                                            ['LL_En', 'bool'],
                                            ]
                                        }
                                        ]
                    },

                    {'AI_PressWiring':[
                                        ['Raw', 'int16'],
                                        ['EU_Raw_Min', 'float'],
                                        ['EU_Raw_Max', 'float'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ['CH_OFF', 'bool'],
                                        ['EU_SUBST', 'float'],
                                        ['HH_Limit', 'float'],
                                        ['H_Limit', 'float'],
                                        ['L_Limit', 'float'],
                                        ['LL_Limit', 'float'],
                                        ['Hyst', 'float'],
                                        {'HMI.Status': [
                                            ['PV', 'float'],
                                            ['SF', 'bool'],
                                            ['HH_En', 'bool'],
                                            ['H_En', 'bool'],
                                            ['L_En', 'bool'],
                                            ['LL_En', 'bool'],
                                            ]
                                        }
                                        ]
                    },

                    {'AI_PressAir':[
                                        ['Raw', 'int16'],
                                        ['EU_Raw_Min', 'float'],
                                        ['EU_Raw_Max', 'float'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ['CH_OFF', 'bool'],
                                        ['EU_SUBST', 'float'],
                                        ['HH_Limit', 'float'],
                                        ['H_Limit', 'float'],
                                        ['L_Limit', 'float'],
                                        ['LL_Limit', 'float'],
                                        ['Hyst', 'float'],
                                        {'HMI.Status': [
                                            ['PV', 'float'],
                                            ['SF', 'bool'],
                                            ['HH_En', 'bool'],
                                            ['H_En', 'bool'],
                                            ['L_En', 'bool'],
                                            ['LL_En', 'bool'],
                                            ]
                                        }
                                        ]
                    },

                    {'AI_LevelL2_1':[
                                        ['Raw', 'int16'],
                                        ['EU_Raw_Min', 'float'],
                                        ['EU_Raw_Max', 'float'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ['CH_OFF', 'bool'],
                                        ['EU_SUBST', 'float'],
                                        ['HH_Limit', 'float'],
                                        ['H_Limit', 'float'],
                                        ['L_Limit', 'float'],
                                        ['LL_Limit', 'float'],
                                        ['Hyst', 'float'],
                                        {'HMI.Status': [
                                            ['PV', 'float'],
                                            ['SF', 'bool'],
                                            ['HH_En', 'bool'],
                                            ['H_En', 'bool'],
                                            ['L_En', 'bool'],
                                            ['LL_En', 'bool'],
                                            ]
                                        }
                                        ]
                    },

                    {'AI_Level_T1':[
                                        ['Raw', 'int16'],
                                        ['EU_Raw_Min', 'float'],
                                        ['EU_Raw_Max', 'float'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ['CH_OFF', 'bool'],
                                        ['EU_SUBST', 'float'],
                                        ['HH_Limit', 'float'],
                                        ['H_Limit', 'float'],
                                        ['L_Limit', 'float'],
                                        ['LL_Limit', 'float'],
                                        ['Hyst', 'float'],
                                        {'HMI.Status': [
                                            ['PV', 'float'],
                                            ['SF', 'bool'],
                                            ['HH_En', 'bool'],
                                            ['H_En', 'bool'],
                                            ['L_En', 'bool'],
                                            ['LL_En', 'bool'],
                                            ]
                                        }
                                        ]
                    },

                    {'AI_Level_T3':[
                                        ['Raw', 'int16'],
                                        ['EU_Raw_Min', 'float'],
                                        ['EU_Raw_Max', 'float'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ['CH_OFF', 'bool'],
                                        ['EU_SUBST', 'float'],
                                        ['HH_Limit', 'float'],
                                        ['H_Limit', 'float'],
                                        ['L_Limit', 'float'],
                                        ['LL_Limit', 'float'],
                                        ['Hyst', 'float'],
                                        {'HMI.Status': [
                                            ['PV', 'float'],
                                            ['SF', 'bool'],
                                            ['HH_En', 'bool'],
                                            ['H_En', 'bool'],
                                            ['L_En', 'bool'],
                                            ['LL_En', 'bool'],
                                            ]
                                        }
                                        ]
                    },

                    {'AI_PressPlate':[
                                        ['Raw', 'int16'],
                                        ['EU_Raw_Min', 'float'],
                                        ['EU_Raw_Max', 'float'],
                                        ['HH_En', 'bool'],
                                        ['H_En', 'bool'],
                                        ['L_En', 'bool'],
                                        ['LL_En', 'bool'],
                                        ['CH_OFF', 'bool'],
                                        ['EU_SUBST', 'float'],
                                        ['HH_Limit', 'float'],
                                        ['H_Limit', 'float'],
                                        ['L_Limit', 'float'],
                                        ['LL_Limit', 'float'],
                                        ['Hyst', 'float'],
                                        {'HMI.Status': [
                                            ['PV', 'float'],
                                            ['SF', 'bool'],
                                            ['HH_En', 'bool'],
                                            ['H_En', 'bool'],
                                            ['L_En', 'bool'],
                                            ['LL_En', 'bool'],
                                            ]
                                        }
                                        ]
                    }
    ],
'Input_Vlv_DB': [{'dbValve_V4':[
                                    ['Cmd', 'int16'],
                                    ['Status_Code', 'int16'],
                                    ['Fault_Code', 'int16'],
                                    ['Enable_Code', 'int16']
                    ]
                    }

    ]
}]


def get_ua_type(type: str):
    types = {
        'INT16': ua.VariantType.Int16,
        'INT32': ua.VariantType.Int32,
        'FLOAT': ua.VariantType.Float,
        'STRING': ua.VariantType.String,
        'UINT16': ua.VariantType.UInt16,
        'UINT32': ua.VariantType.UInt32,
        'BOOL': ua.VariantType.Boolean
    }
    return types.get(type.upper(), ua.VariantType.String)


def get_init_value(type: str):
    types = {
        'INT16': randint(0, 10),
        'INT32': randint(1, 10),
        'FLOAT': uniform(0.01, 9.99),
        'STRING': choice("abcdefgh"),
        'UINT16': randint(1, 10),
        'UINT32': randint(1, 10),
        'BOOL': choice([True, False])
    }
    return types.get(type.upper(), 'undefined')

def create_tag(addobj, prefix:str, tag:list):

    var = addobj.add_variable(
        ua.NodeId(f'PLC.Blocks.{prefix}.{tag[0]}', idx, ua.NodeIdType.String),
        tag[0],
        get_init_value(tag[1]),
        varianttype=get_ua_type(tag[1])
    )
    var.set_writable()  # <-- теперь клиент может изменять значение


for db in obj_dict:
    for db_key, db_value in db.items():
        db_obj = objects.add_object(idx, db_key)
        print(f'item_key = {db_key}')
        print(f'tags_value = {db_value}')
        for item in db_value:
            print(f'tags in item = {item}')
            for item_key, item_value in item.items():
                item_obj = db_obj.add_object(idx, item_key)
                for socket in item_value:
                    # Обработка вложенный в структуры тегов
                    if type(socket) is dict:
                        for socket_key, socket_values in socket.items():
                            socket_obj = item_obj.add_object(idx, socket_key)
                            for tag in socket_values:
                                print(f'socket_tags in tags dict = {tag}')
                                create_tag(socket_obj, f'{db_key}.{item_key}.{socket_key}', tag)
                    # Теги без структуры
                    if type(socket) is list:
                        print(f'tags no sockets = {socket}')
                        create_tag(item_obj, f'{db_key}.{item_key}', socket)


# Запускаем сервер
if __name__ == "__main__":
    try:
        objects.add_variable(ua.NodeId('IS_ACTIVE', idx, ua.NodeIdType.String), 'IS_ACTIVE', True, varianttype=ua.VariantType.Boolean)
        print("Starting OPC UA Server...")
        server.start()
        print("Server started at:", server.endpoint)
        print("Press Ctrl+C to stop")
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping server...")
        server.stop()
        print("Server stopped.")

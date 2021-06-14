#########################################################                        
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################

from protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from protocol.mcbe.packet.mcbe_packet import mcbe_packet

class set_entity_data_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.set_actor_data_packet
        
    def decode_payload(self) -> None:
        self.runtime_entity_id: int = self.read_var_long()
        self.metadata: dict = self.read_metadata_dictionary()
        self.tick: int = self.read_var_int()
        
    def encode_payload(self) -> None:
        self.write_var_long(self.runtime_entity_id)
        self.write_metadata_dictionary(self.metadata)
        self.write_var_int(self.tick)

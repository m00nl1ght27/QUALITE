#!/usr/bin/env python3
 
import argparse
 
'''FUNCTIONS'''
def get_Number(string_Hex_Chain):
        converted_Number = ''
        for i in range(0,len(string_Hex_Chain),2):
                converted_Number = converted_Number + ''.join(string_Hex_Chain[i:i+2][::-1])
        converted_Number = '+' + converted_Number
        if converted_Number[len(string_Hex_Chain)] == 'f':
                converted_Number = converted_Number[0:len(string_Hex_Chain)]
       
        return converted_Number
 
def decypher_PDU_SMS(UD_String):
        liste_Hex = []
        for i in range(0,len(UD_String),2):
                liste_Hex.append(UD_String[i:i+2])
 
        bin_String = ""
        for hex_Number in liste_Hex:
                bin_Number_String = "{0:08b}".format(int(hex_Number, 16))
                bin_String = bin_Number_String + bin_String
 
        decoded_SMS_Message = ""
        for i in range(len(bin_String)-7,0,-7):
                new_Bin_String = "0" + bin_String[i:i+7]
                new_Hex_Value = hex(int(new_Bin_String, 2))
                decoded_SMS_Message += bytes.fromhex(new_Hex_Value[2:]).decode()
 
        return decoded_SMS_Message
 
def get_Date(string_Hex_Chain):
        converted_Date = ''
        for i in range(0,len(string_Hex_Chain),2):
                converted_Date = converted_Date + ''.join(string_Hex_Chain[i:i+2][::-1]) + '/' 
        converted_Date = converted_Date[0:len(converted_Date)-1]
       
        return converted_Date
 
def get_Time(string_Hex_Chain):
        converted_Time = ''
        for i in range(0,len(string_Hex_Chain),2):
                converted_Time = converted_Time + ''.join(string_Hex_Chain[i:i+2][::-1]) + ':' 
        converted_Time = converted_Time[0:len(converted_Time)-1]
       
        return converted_Time
 
def get_GMT(string_Hex_Chain):
        converted_GMT = string_Hex_Chain[1] + string_Hex_Chain[0]
 
        return converted_GMT
 
 
'''MAIN PROGRAM'''
if __name__ == '__main__':
        # On crée un parser pour rappeler qu'il faut renseigner le fichier PNG en argument
        parser = argparse.ArgumentParser(description='PDU Interpreter from Fwed')
        parser.add_argument('PDU_String', type=str, help='Please provide PDU string as argument')
        args = parser.parse_args()
       
        pdu_Info = args.PDU_String
 
        SMSC_Length = int(pdu_Info[0:2])
        SMSC_Address_Type = int(pdu_Info[2:4])
 
        index_End_SMSC_Info = 4+2*(SMSC_Length-1)
        temp_Index = index_End_SMSC_Info
 
        service_Center_Number_String = pdu_Info[4:temp_Index]
        converted_SCN = get_Number(service_Center_Number_String)
 
        first_Octet_SMS_Deliver = pdu_Info[temp_Index:temp_Index+2]
        temp_Index += 2
        sender_Number_Length = int(pdu_Info[temp_Index:temp_Index+2],16)
        temp_Index += 2
        sender_Number_Address_Type = pdu_Info[temp_Index:temp_Index+2]
        temp_Index += 2
 
        sender_Number_String = pdu_Info[temp_Index:temp_Index+sender_Number_Length+1]
        converted_SN = get_Number(sender_Number_String)
        temp_Index += sender_Number_Length+1
 
        TP_PID = pdu_Info[temp_Index:temp_Index+2]
        temp_Index += 2
 
        TP_DCS = pdu_Info[temp_Index:temp_Index+2]
        temp_Index += 2
 
        time_Date = get_Date(pdu_Info[temp_Index:temp_Index+(3*2)])
        temp_Index += 3*2
 
        time_Hour = get_Time(pdu_Info[temp_Index:temp_Index+(3*2)])
        temp_Index += 3*2
 
        time_GMT = get_GMT(pdu_Info[temp_Index:temp_Index+2])
        temp_Index += 2
 
        TP_UDL = pdu_Info[temp_Index:temp_Index+2]
        temp_Index += 2
 
        TP_UD = pdu_Info[temp_Index::]
 
        #Dechiffrement SMS
        decoded_SMS = decypher_PDU_SMS(TP_UD)
 
        #Affichage
        print("Taille de l'en-tête SMSC : %d" %(SMSC_Length))
        print("Type d'adresse (91 = format international) : %d" %(SMSC_Address_Type))
        print("Numero du Service Center : %s" %(converted_SCN))
        print("Type SMS (04 = SMS-DELIVER / 11 = SMS-SUBMIT) : %s" %(first_Octet_SMS_Deliver))
        print("Taille du numéro du sender : %d" %(sender_Number_Length))
        print("Type d'adresse (91 = format international) : %s" %(sender_Number_Address_Type))
        print("Numero du sender : %s" %(converted_SN))
        print("Identifiant du protocole (00 = PDU SMS) : %s" %(TP_PID))
        print("Spécification de l'encoding de la donnée : %s" %(TP_DCS))
        print("Date : %s" %(time_Date))
        print("Heure : %s" %(time_Hour))
        print("Fuseau horaire (GMT) : +%s" %(time_GMT))
        print("Taille du message (nombre de septets, en hexa): %s" %(TP_UDL))
        print("Message SMS : %s" %(decoded_SMS))


import Utilities as Ut, Market_Data_Utilities as Mdu, Ineractive_Data_Utilities as Idu


print("Performing initial login...")
Connect_Dict = Ut.Initial_Login_Modified("ATM011948")
Market_Xt = Connect_Dict['Market_Xt']
Interactive_Xt = Connect_Dict['Interactive_Xt']
ClientID = Connect_Dict['ClientID']
print("Login successful")

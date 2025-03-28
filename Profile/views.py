from django.shortcuts import render
from Register.models import UserAccount
def index(request):
    ref_code_final_result = ""
    users_data = UserAccount.objects.values_list("id", "username" ,"email" , "phone_number" ,"AC" ,"Date_Joined" ,"Ref_Code" ,"is_RevardClaimed")
    users_data = list(users_data)
    user_data = []
    for i in users_data :
        if i[1] == str(request.user) :
            user_data = i
    user_data = {
        'id' : user_data[0] ,
        'username' : user_data[1] ,
        'email' : user_data[2] ,
        'phone_number' : user_data[3] ,
        'AC' : user_data[4] ,
        'Date_Joined' : str(user_data[5]) ,
        'Ref_Code' : str(user_data[6]) ,
        'is_RevardClaimed' : user_data[7]
    }
    if request.method == "POST":
        if not user_data["is_RevardClaimed"]:
            if user_data["Ref_Code"] != str(request.POST["referral-code"]) : 
                if len(UserAccount.objects.filter(Ref_Code = str(request.POST["referral-code"])).values_list("AC")) != 0 :
                    selected_user_AC = list(UserAccount.objects.filter(Ref_Code = str(request.POST["referral-code"])).values_list("AC")[0])[0]
                    current_user_AC = list(UserAccount.objects.filter(username = str(request.user)).values_list("AC")[0])[0]
                    UserAccount.objects.filter(Ref_Code = str(request.POST["referral-code"])).update(AC = selected_user_AC + 10)
                    UserAccount.objects.filter(username = str(request.user)).update(AC = current_user_AC + 10)
                    UserAccount.objects.filter(username = str(request.user)).update(is_RevardClaimed = True)
                    ref_code_final_result = "You have successfully received your prize."
                else : ref_code_final_result = "Invalid Referral Code"
            else : ref_code_final_result = "You Can\'t Use Your Referral Code For Yourself"
        else : ref_code_final_result = "You Received Your Price Befor"
        print(ref_code_final_result)
    return render(request , 'profile/index.htm' ,{'user_data' : user_data , 'ref_code_final_result' : ref_code_final_result})
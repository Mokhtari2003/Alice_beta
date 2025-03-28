import secrets
import string
def Ref_Code_generator(length=6 ,ref_codes = []) :
    
    chars = string.ascii_uppercase + string.digits
    new_ref_code = ''.join(secrets.choice(chars) for _ in range(length))
    for i in ref_codes:
        if i == new_ref_code :
            new_ref_code = Ref_Code_generator(ref_codes = ref_codes)
    return new_ref_code


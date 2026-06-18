from fastapi import Depends
from fastapi import HTTPException

from services.auth_service import get_current_user

def require_role(required_role : str):
    
    def role_checker(current_user = Depends(get_current_user)):

        if current_user.role != required_role:

            raise HTTPException(
                status_code = 403,
                details = "Access Denied!"
            )
        
        return current_user
    
    return role_checker
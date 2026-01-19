def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def admin_only(func):
    def wrapper(*args, **kwargs):
        role = kwargs.get("role", "user")
        if role != "admin":
            print("Access Denied: Admin privileges required")
            return
        return func(*args, **kwargs)
    return wrapper

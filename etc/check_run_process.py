import psutil

# Check if there is any running process that contains the given name processName.
def checkIfProcessRunning(processName: str) -> bool:
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

def notify_processing_app_name() -> str:
    app_list = [
        'slack', 'chrome', 'kakaotalk', 'telegram', 'melon', 'youtube',
        'flo', 'bugs', 'genie', 'youtube music',
    ]
    message = ''

    for app in app_list:
        if checkIfProcessRunning(app):
            message += f'{app} 어플리케이션이 현재 활성화돼 있습니다.\n'

    return message if message else '활성화된 어플리케이션이 없습니다.'

if __name__ == '__main__':
    print(notify_processing_app_name())
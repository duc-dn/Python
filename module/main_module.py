import codexplore
from codexplore import print_message

def main():
    emails = ['codexplore@developer.dev', 'manchesterunited@winner.mu', 'ducdo@yahoo.com']
    for email in emails:
        username, domain = codexplore.emailProcess(email)
        print_message(username, domain)

if __name__ == '__main__':
    main()

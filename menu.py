from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

table = Table(title="Info Table")
table.add_column("[blue underline]Realeased", style="cyan")
table.add_column("[bold red]Test", style="cyan")
table.add_row("1", "2")

for i in track(range(1), description=""):
    time.sleep(0.5)

console = Console()

menu_options = {
    1: 'Print Table',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     console.print(table)

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

# table = Table(title="Info Table")
#
# table.add_column("[blue underline]Realeased", style="cyan")
# table.add_column("[bold red]Test", style="cyan")
#
# for i in track(range(10), description="Processing..."):
#     time.sleep(0.5)
#
# console = Console()
# console.print(table)

from booking.booking import Booking

with Booking() as bot:
    # chromedriver.exe must be in same folder as run.py
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go(input("Where would you like to go? "))
    bot.select_dates(check_in_date=input("What is the check-in date? (YYYY-MM-DD) "), 
                    check_out_date=input("What is the check-out date? (YYYY-MM-DD) "))
    bot.select_adults(int(input("How many adults? ")))
    bot.click_search()
    bot.remove_map()
    bot.apply_filtrations()
    bot.refresh()
    bot.remove_map()
    bot.report_results()
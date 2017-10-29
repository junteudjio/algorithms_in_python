__author__ = 'Junior Teudjio'


def draw_ruler(number_of_inches, major_tick_length):
    def draw_inch_containt(tick_length):
        if tick_length > 0:
            draw_inch_containt(tick_length - 1)
            print '-'*tick_length
            draw_inch_containt(tick_length - 1)


    def draw_ruler_helper(current_inch):
        print '-' * major_tick_length, ' ', current_inch
        if number_of_inches == current_inch:
            return
        else:
            draw_inch_containt(major_tick_length - 1)
            draw_ruler_helper(current_inch + 1)


    draw_ruler_helper(0)




if __name__ == '__main__':
    print 'Ruler of 2 inches with major tick length of 4'
    draw_ruler(number_of_inches=2, major_tick_length=4)
    print


    print 'Ruler of 1 inches with major tick length of 5'
    draw_ruler(number_of_inches=1, major_tick_length=5)
    print


    print 'Ruler of 3 inches with major tick length of 3'
    draw_ruler(number_of_inches=3, major_tick_length=3)
    print

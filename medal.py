########################################################################################################################
# def rank_team():
# This just opens the file. It will then read the file using a csv reader which is imported from the CSV module.
# It will then get the header by missing the first row and storing it in its own variable.
# After that, then it will go row in row and collect the data and store it in a data variable.
#
# After it has read the file it will then write and open a new file with all the data collected from the medal.csv.
# When it's opened it, it will then write the header (we collected that in the read), and then we write the rows using
# our own lambda sorting function.
#
# Once it's done all of that it will then start the function rank_team('medal.csv')
########################################################################################################################
import csv


def rank_team(file_name):
    # This opens and reads the files and takes the rows.
    # csv header to just 'separate' from the rest of the body
    with open('medal.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skips the header and will then will read each of the rows in the CSV file.
        csv_header = next(csv_reader)
        data = [row for row in csv_reader]
        print('Check the file for medal_table.\nThe new CSV will be located where you launched the py.')

    # This generates the new file!
    # Using w+ will write the file and it will be called medal_table.csv. Then with the new file we should write into it
    # With the header we got from reading it we can put it in the file as it's own separate header. Then just sort the
    # body.
    new_file_medal = open('medal_table.csv', 'w+')
    with new_file_medal:
        # This write variable will be used to write the rows of the header and the data within it.
        write = csv.writer(new_file_medal)
        write.writerow(csv_header)
        # This writes out the data and then this sorts out the data in a reversed order using Lambda
        write.writerows(reversed(sorted(data, key=lambda medals: (medals[1]))))
    pass


rank_team('medal.csv')
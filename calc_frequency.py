import csv
import ast
from collections import Counter, OrderedDict

with open("./quotations_and_speeches_v2.0.csv", "r") as file:
    reader = csv.reader(file)
    all_locations = []
    all_organizations = []
    all_persons = []
    next(reader)
    for row in reader:

        location = row[3]
        organization = row[4]
        person = row[5]

        location = ast.literal_eval(location)
        organization = ast.literal_eval(organization)
        person = ast.literal_eval(person)
        all_locations += location
        all_organizations += organization
        all_persons += person

# loc_counter = dict(Counter(all_locations).most_common(20))
# org_counter = dict(Counter(all_organizations).most_common(20))
# per_counter = dict(Counter(all_persons).most_common(20))

loc_counter = dict(Counter(all_locations))
org_counter = dict(Counter(all_organizations))
per_counter = dict(Counter(all_persons))

ordered_loc = OrderedDict(sorted(loc_counter.items(), key=lambda t: t[1]))
ordered_org = OrderedDict(sorted(org_counter.items(), key=lambda t: t[1]))
ordered_per = OrderedDict(sorted(per_counter.items(), key=lambda t: t[1]))

# with open("./location_count.csv", "a") as out:
#     writer = csv.writer(out)
#     for k, v in reversed(ordered_loc.items()):
#         writer.writerow([k, v])

# with open("./organization_count.csv", "a") as out:
#     writer = csv.writer(out)
#     for k, v in reversed(ordered_org.items()):
#         writer.writerow([k, v])

with open("./Scraped data/person_count.csv", "a") as out:
    writer = csv.writer(out)
    for k, v in reversed(ordered_per.items()):
        writer.writerow([k, v])

# DO NOT DELETE THE COMMENTS!

from spacy.en import English
nlp = English()

sentences = ["Sources said that during the last 20 years (from 1994 to 2013), the Directorate General of Drug Administration (DGDA) authorities received only 50 ADR reports, among which only 10 reports were completed properly.",
             "Meanwhile, several senior officials at DGDA said the deaths of four babies at a Tangail hospital on Friday were the result of doctors not reporting on ADR, which would have allowed them to understand the drug quality earlier.",
             "DGDA director Selim Barami told the Dhaka Tribune that the authorities revived the ADRAC on April 25, with departmental heads of different medical colleges included in the committee.",
             "Chairman of National Human Rights Commission Professor Mizanur Rahman said the trial of Oishee Rahman, accused of killing her parents, should be conducted under the Children Act enacted in 2013, not under the 1974 law."
             "Mizanur Rahman was speaking at a round table conference held at a local restaurant on Monday."
             "The tribunal said getting a signal from Mujaheed after talks with the army personnel, some razakars and non-Bangalee people took Ranjit to the house of one Abdur Rashid.",
             "The witness said on April 6 or 7 that year, he along with Quiyum and Salman F Rahman, travelled to Pakistan.",
             "Sources said the victim, a Class IX student, was visiting Lalbagh with her boyfriend Sujon and was on her way home at Mirpur when she was grabbed and taken to an under-construction building, where she was raped.",
             "The victim filed a case in this regard with Lalbagh police station against three men, one of whom she identified as Saikat Islam Rana, 23, a resident of Lalbagh and a shop attendant at Gausia market, sources said.",
             "Sujon then notified police, and a police patrol team started looking for her and found her in the under-construction building around 4:30am, said Inspector Paritosh Chandra of Lalbagh police station.",
             "Just five days ago Muhith said the government would not rather take last $280m under the $1bn ECF than meeting a condition of international audit to the country's loan fuel oil importer.",
             "Fuel prices were $80, $90 and $120 per barrel in various times in the global market, but the BPC had kept the prices unchanged in local market over the years, Muhith said.",
             "The officer-in-charge of Bangabandhu bridge west police outpost said Rangpur-bound Sabbir Hossain Paribahan from Chittagong and Dhaka-bound Azad Paribahan from Gaibandha collided head-on around 5am, leaving 12 dead on the spot."
             ]
subject = ""
indirect_object = ""
direct_object = ""
for i in sentences:
    parsed_text = nlp(i)

    # get token dependencies
    for text in parsed_text:
        # subject would be
        if text.dep_ == "nsubj":
            subject = text.orth_
        # iobj for indirect object
        if text.dep_ == "iobj":
            indirect_object = text.orth_
        # dobj for direct object
        if text.dep_ == "dobj":
            direct_object = text.orth_

    print(i)
    print("subject: ", subject)
    print("direct object: ", direct_object)
    print("indirect object: ", indirect_object)
    print("-" * 30)

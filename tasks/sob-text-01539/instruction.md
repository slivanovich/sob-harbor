Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Culture of Telangana: The Indian state of Telangana has a cultural history of about 5,000 years, the region emerged as the foremost centre of culture in Indian subcontinent during the Hindu Kings of Kakatiya dynasty and the Muslim rulers of Qutb Shahi and Asaf Jahi Dynasty—(also known as the Nizams of Hyderabad) , the rulers patronage and interest for arts and culture had transformed Telangana into a unique multi cultural region where two different cultures coexist parallel to each other, thus making Telangana the representative of the Deccan Plateau and its heritage with Warangal and Hyderabad being its epicenter.  The regions major cultural events celebrated are "Kakatiya Festival" and Deccan Festival along with religious festivals of Bonalu, Bathukamma, Dussehra, Ugadi, Sankranthi, Milad un Nabi and Ramadan.

Qurain Cultural Festival: The Qurain Cultural Festival is Kuwait's leading arts festival.  It is sponsored by the National Council for Culture, Arts and Letters, Kuwait and its purpose is to enhance the artistic and cultural movement in Kuwait.  It includes theatre performances, literary events, the exhibitions of the visual arts and other cultural events.  As of 2010 it has run 16 times since its inauguration in 1994.

Adelaide Festival: The Adelaide Festival of Arts, also known as the Adelaide Festival, is an arts festival held annually in the South Australian capital of Adelaide.  It is considered to be one of the world's major celebrations of the arts, and a pre-eminent cultural event in Australia.

ImagineNATIVE Film + Media Arts Festival: The imagineNATIVE Film + Media Arts Festival is the world's largest Indigenous film and media arts festival, held annually in Toronto in the month of October.  The festival focuses on the film, video, radio, and new media work of Indigenous, Aboriginal and First Peoples from around the world.  The festival includes screenings, parties, panel discussions, and cultural events.

Athens Festival: Athens – Epidaurus Festival is an annual arts festival that takes place in Athens and Epidaurus, from May to October.  It is one of the most famous festivals in Greece.  The festival includes musical, theatrical and other cultural events.

Hamazkayin: Hamazkayin (Armenian: Համազգային ), short for Hamazkayin Armenian Educational and Cultural Society, is a major cultural organization of the Armenian Diaspora, with a presence in every significant Armenian community worldwide.  In addition to organizing cultural events in local Armenian communities, the Hamazkayin runs three schools, publishes books through its printing press, maintains bookstores, publishes a monthly literary magazine, "Pakin" (Armenian: Բագին ), and organizes the "Hamazkayin Forum".  Hamazkayin enjoys the support of a wide segment of the Armenian community and encourages active participation to the events sponsored by the community.  Hamazkayin sponsors and organizes many cultural events, such as concerts by renowned artists, scientific seminars, film festivals, literary lectures and book reviews.  In the United States, the Hamazkayin Armenian Educational and Cultural Society was established as a non profit organization in 1970.

Boyacá International Cultural Festival: The Boyacá International Cultural Festival (Spanish: Festival Internacional de la Cultura de Boyacá or just FIC) is one of the major international cultural events held annually in Colombia.  The festival presents works in various arts such as music, theater, dance, literature, Academy, Visual Arts, Cinema - Audiovisual, Cultural Heritage cultural exchanges and meetings at various stages in the city of Tunja since 1973.  Artists from different corners of the world intertwine their knowledge and their cultures into one universal feeling, through the medium of art, the best mechanism to achieve peace and brotherhood of people.  The FIC gathers thousands of artists and has more than 300,000 visits to about 500 events per version.  The festival is considered to be one of the most representative of music, dance, the arts, theater, cultural heritage, literature, cinema and expressions of human sensibility.

Brodsko kolo: Brodsko kolo (English: The kolo (dance) of Brod ) is an annual festival of folklore held in Slavonski Brod, Croatia.  The festival was founded in 1962, and is considered one of the major cultural events of the whole of Slavonia, together with "Vinkovačke jeseni" and "Đakovački vezovi".  Until 1991 it was referred to under the generic name "Smotra folklora" (Folklore festival).

Rose English: Rose English is a British artist working in performance, installation, theatre, dance and film.  She has been writing, directing and performing her own work for over thirty five years in venues as various as Tate Britain; Royal Court Theatre; Queen Elizabeth Hall; the Adelaide Festival; and Lincoln Center, New York.  Her productions feature a diversity of co-performers including musicians, dancers, circus performers, magicians and horses.

Chris Tally Evans: Chris Tally Evans is a British disabled artist, actor, director and writer.  He trained at the Royal Welsh College of Music and Drama as a performer and graduated from Trinity College, London with a teaching diploma.  Evans' interest in theatre and music started as a teenager when he joined West Glamorgan Youth Theatre and West Glamorgan Youth Arts Company as an actor, dancer and musician.  He was lead guitarist for the West Glamorgan Youth Arts Company production of Leonard Bernstein's "Mass" at Swansea's Brangwyn Hall and London's Wembley Arena and was a dancer in Vaughan Williams' "Job" at a performance attended by Prince Charles and Princess Diana in 1981.  In both these productions he shared the stage with Russell T Davies, writer and producer of Dr Who.  By the age of 14 he was playing the guitar semi-professionally in pubs and clubs in the Swansea area, as well as for a number of theatre shows.  For two years at this time he was lead guitarist in the backing band of a very young Catherine Zeta-Jones.  Later Evans played in a number of bands including the electric folk band Straight From the Wood who chalked up memorable appearances at Club Ifor Bach, Cardiff, Gwyl Pontardawe Festival and the Village Pump Folk Festival in Trowbridge.  Evans has had both poetry and prose published, directed many theatre productions and has performed himself in the United States, Canada, Poland and New Zealand.  His film work was exhibited at the John F. Kennedy Center for the Performing Arts, Washington DC, in 2011.  The Arts Council of Wales granted Evans a Major Creative Wales Award in 2009 and he performed work created at this time at the InterACT Disability Arts Festival in Auckland, New Zealand.  His unlimited commission, "Turning Points", was shown in the Southbank Centre, London during the 2012 Paralympic Games and then went on to be exhibited in Doha, Qatar in 2013 as part of the Middle East’s first ever disability arts festival.  He has featured in HTV’s award winning documentary, One in Six, on BBC 2W’s The Arts Show, and wrote and performed a 5-part series for BBC Radio 4 called "My Mile of the River".  His March 2014 production, "21st Century Dinosaurs", with a visually impaired cast, was reviewed favourably by Sarah Finch of National Theatre Wales.  He wrote, performed and made video content for National Theatre Wales/Celf o Gwmpas' Big Democracy Project which responded to the question "Are disabled people an easy target for the cuts?"  in June 2015.  In 2015 he was appointed a National Adviser to the Arts Council of Wales.

Question: Rose English has performed her work at the arts festival that is one of the major cultural events in what country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist who performed."
    },
    "festival_name": {
      "type": "string",
      "description": "The name of the arts festival where the artist performed."
    },
    "festival_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the festival is held."
        },
        "country": {
          "type": "string",
          "description": "The country where the festival is held."
        }
      },
      "required": [
        "city",
        "country"
      ],
      "additionalProperties": false
    },
    "festival_description_keywords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Keywords describing the significance or type of the festival."
    }
  },
  "required": [
    "artist_name",
    "festival_name",
    "festival_location",
    "festival_description_keywords"
  ],
  "additionalProperties": false
}

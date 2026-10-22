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
1982 Virginia vs. Chaminade men's basketball game: The 1982 Virginia vs. Chaminade men's basketball game was a college basketball game between the Virginia Cavaliers of the University of Virginia and the Chaminade Silverswords of Chaminade University of Honolulu.  The contest was held on December 23, 1982, at the Honolulu International Center in Honolulu, Hawaii.  The Silverswords, then a National Association of Intercollegiate Athletics (NAIA) member, defeated the Cavaliers, who were the National Collegiate Athletic Association's (NCAA) top-ranked team, 77–72.  Chaminade's victory over a Virginia team that included three-time national player of the year Ralph Sampson has been called college basketball's "biggest upset" by multiple publications.

Ka Haka ‘Ula O Ke‘elikōlani, College of Hawaiian Language: Ka Haka ‘Ula O Ke‘elikōlani, College of Hawaiian Language

Saint Louis School: Saint Louis School, located in the neighborhood of Kaimuki in Honolulu, Hawaii, is a historic Roman Catholic college preparatory school for boys.  It was founded in 1846 to serve the needs of early Hawaiian Catholics in the former Kingdom of Hawaii.  Located within the Roman Catholic Diocese of Honolulu, it is affiliated with the Society of Mary, a religious order of brothers and priests called the Marianists who also administer Chaminade University of Honolulu, formerly the college section of Saint Louis School.  It is located near Sacred Hearts Academy, a girls' school founded by the Congregation of the Sacred Hearts of Jesus and Mary, and both schools hold joint programs such as cultural festivals and the JROTC.

Ulukau: The Hawaiian Electronic Library: Ulukau: The Hawaiian Electronic Library is an online, digital library of Native Hawaiian reference material for cultural and Hawaiian language studies.  The services are free and are provided and maintained by "Kahaka ‘Ula O Ke’elikolani" College of Hawaiian Language at the University of Hawaii at Hilo and "Ka Waihona Puke 'Ōiwi" Native Hawaiian Library at Alu Like.  The site is available worldwide, containing Hawaiian language newspapers, books and other resources with mirror sites in both English and Native Hawaiian.  Western studies of Hawaii tend to ignore the Hawaiian language newspapers.  These digital archives serve to make these sources available for educational and scholarly work.  The collaboration between Ho‘olaupa‘i, Hale Kaumo‘o and Alu Like contain the largest collection of digitized native language newspapers in the Pacific with nearly 125,000 pages accessible within Ulukau.  The library's digital dictionary, is "Nā Puke Wehewehe ‘Ōlelo Hawai‘i".  In the Hawaiian language the term "Puke Wehewehe ‘Ōlelo" means "dictionary".  Photographer Ed Greevy, who helped illustrate several books including: ""A Nation Rising: Hawaiian Movements for Life, Land, and Sovereignty"", has donated a good deal of his work to the Hawaiian electronic library.

Chaminade Silverswords: The Chaminade Silverswords are the 10 varsity athletic teams that represent Chaminade University of Honolulu, located in Honolulu, Hawaii, in NCAA Division II intercollegiate sports.  The Silverswords compete as members of the Pacific West Conference.  Chaminade University of Honolulu's team name is the "Silverswords," a reference to a Hawaiian plant prized for its beauty and ability to withstand harsh conditions.

Chaminade University of Honolulu: Chaminade University of Honolulu is a private co-educational university in Honolulu, Hawaii, United States.  Founded in 1955 by the Society of Mary, a Roman Catholic religious order also known as the Marianists, Chaminade is located in the historic Kaimuki district of Honolulu at the base of St. Louis Heights.  Chaminade offers bachelor's degrees in 23 fields of study and five master's degree programs.  The school specializes in biology, business, criminal justice, education, forensic sciences, interior design, nursing, and religious studies.  Chaminade University is accredited by the Western Association of Schools and Colleges (WASC).

Kau High and Pahala Elementary School: Ka'u High & Pahala Elementary School is a public, co-educational high school, middle school and elementary school of the Hawaii State Department of Education.  It serves kindergarten through twelfth grade and was established in 1881.  It was the first high school established on the Big Island of Hawaii and the third public high school established in Hawaii, after Lahainaluna High School on Maui and President William McKinley High School, formerly Honolulu High School, on Oahu.  The high school was established after the 1876 opening of the Hawaiian Agricultural Company (a predecessor of the Ka'u Sugar Company), at the time one of the largest most remote sugarcane plantations in the Kingdom of Hawaii.  The plantation employed a large number of immigrants who wanted their children to have a high school education; Honokaa High & Intermediate School was established on the north end of the island eight years later for similar reasons.

Maui Invitational Tournament: The Maui Invitational, currently known as the Maui Jim Maui Invitational, is an annual early-season college basketball tournament that takes place Thanksgiving Week in Lahaina, Hawaii, at the Lahaina Civic Center on the island of Maui.  It is hosted by Chaminade University of Honolulu, an NCAA Division II school.  Seven NCAA Division I men's basketball teams are invited to Maui to complete the field.  The Maui Invitational has been played since 1984, is carried by ESPN.  Maui Jim became the title sponsor of the tournament in 2015; the previous fourteen tournaments sponsored by EA Sports.

Keiki Kawaiʻaeʻa: Keiki Kawaiʻaeʻa is an Associate Professor at the University of Hawaii at Hilo where she serves as Director of the Ka Haka ʻUla O Keʻelikōlani College of Hawaiian Language.  Dr. Kawaiʻaeʻa holds a doctorate from Union Institute & University, a Professional Diploma in Elementary Education from Chaminade University, a Master of Education degree in Curriculum & Instruction from the University of Hawaiʻi at Mānoa, and a BA in Hawaiian Studies from the University of Hawaiʻi at Mānoa.

Sacred Hearts Academy: Sacred Hearts Academy also known as Sacred Hearts or SHA is located on 3253 Waiʻ alae Avenue, in the town of Kaimuki in Honolulu, Hawaiʻ i, is a historic Roman Catholic college preparatory school for girls founded in 1909 to serve the needs of early Hawaiʻ i Catholics in the former Territory of Hawaiʻ i.  The school maintains a special relationship with Chaminade University of Honolulu and the all-boys Saint Louis School, both administered by the Society of Mary.

Question: Keiki Kawaiʻaeʻa is an Associate Professor at the University of Hawaii at Hilo where she serves as Director of the Ka Haka ʻUla O Keʻelikōlani College of Hawaiian Language, she holds a Professional Diploma in Elementary Education from Chaminade University, Chaminade University of Honolulu is a private, co-educational university in Honolulu, Hawaii, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "university_name": {
      "type": "string",
      "description": "The name of the university."
    },
    "city": {
      "type": "string",
      "description": "The city where the university is located."
    },
    "state": {
      "type": "string",
      "description": "The state where the university is located."
    },
    "country": {
      "type": "string",
      "description": "The country where the university is located."
    }
  },
  "required": [
    "university_name",
    "city",
    "state",
    "country"
  ],
  "additionalProperties": false
}

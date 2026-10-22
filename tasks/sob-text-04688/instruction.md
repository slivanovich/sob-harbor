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
Deedar (1951 film): Deedar (Hindi: दीदार , "glance") is a 1951 Bollywood Hindi language film directed by Nitin Bose and starring Ashok Kumar, Dilip Kumar, Nargis and Nimmi.  A story of unfulfilled love, when hero's childhood love is separated from him due to class inequalities.  It is one of noted tragedies made in early Hindi cinema.  It became a popular film of the Golden era and further established Dilip Kumar as "King of Tragedy".

Hamaari Beti Raaj Karegi: Hamaari Beti Raaj Karegi is an Indian television drama series that airs on Sahara One channel.  The series is premiered on 20 December 2010 .  The series starrs known Bollywood actress Saira Banu in an important role.  The show was about to end but it was so popular they decided to give it a second chance.

Paigham: Paigham ("Message") is a 1959 Hindi film produced and directed by S. S. Vasan.  The film stars Dilip Kumar, Vyjayanthimala, Raaj Kumar, Saroja Devi, Motilal, and Johnny Walker.  The film's music is by C. Ramachandra.  This was the first time Dilip and Raaj Kumar appeared in a film together.  (They later appeared together once again over three decades later for the 1991 film "Saudagar").

Kranti: Kranti (English: "Revolution") is a 1981 Indian Hindi film, produced and directed by Manoj Kumar, with the story written by Salim-Javed.  It stars Manoj Kumar along with an ensemble cast consisting of Dilip Kumar, Shashi Kapoor, Hema Malini, Shatrughan Sinha, Parveen Babi, Sarika, Prem Chopra, Madan Puri, Paintal and Pradeep Kumar.  The film marked the return of Dilip Kumar after a five-year hiatus.

Karma (1986 film): Karma (Hindi:कर्मा) is a 1986 Indian action film directed by Subhash Ghai and featuring an ensemble cast including Dilip Kumar, Nutan, Naseeruddin Shah, Jackie Shroff, Anil Kapoor, Poonam Dhillon, Sridevi and Anupam Kher.  The film reunites Subhash Ghai and Dilip Kumar after the success of their last film together "Vidhaata" (1982).  The film also marked the first time Dilip Kumar was paired with veteran actress Nutan.  The film was a huge success at box office.

Leshi Singh: Leshi singh (Hindi: लेशी सिंह ) is a JDU member of the Legislative Assembly from the Dhamdaha seat in Bihar.  She has been made the minister in nitish kumar cabinet, and has been the president of Bihar state women commission.  In the 2010 state assembly elections, Leshi Singh of JD(U) won the Dhamdaha assembly defeating his nearest rival Irshad Ahmad Khan of Congress. [3] Contests in most years were multi cornered but only winners and runners are being mentioned.  Dilip Kumar Yadav of RJD defeated Leshi Singh of JD(U) in October 2005.  Leshi Singh of JD(U) defeated Dilip Kumar Yadav of RJD in February 2005.  Leshi Singh of Samta Party defeated Dilip Kumar Yadav of RJD in 2000.  She became minister in Nitish kumar cabinet in 2014 when both women minister Renu kushwaha and Parveen amanullah resigned.  During Jeetan Ram Manjhi incident, she also resigned.  When Nitish Kumar became chiefminister she was again inducted as minister.

Gunga Jumna: Gunga Jumna (गंगा जमना, also transliterated as Ganga Jamuna or Ganga Jamna) is a 1961 Bollywood dacoit crime drama film, produced in Technicolor, written and produced by Dilip Kumar, and directed by Nitin Bose, with dialogues written by Wajahat Mirza.  The film stars Dilip Kumar, Vyjayanthimala and Nasir Khan in leading roles, and Azra, Kanhaiyalal, Anwar Hussain, Nazir Hussain and Leela Chitnis in supporting roles, along with Helen appearing in an item number.  Notable for its use of the Bhojpuri dialect and its rustic setting, the film features real life brothers Dilip Kumar (Muhammad Yusuf Khan) and Nasir Khan in the title roles, tells the story of two brothers, Gunga and Jumna, and their poignancy on the opposite sides of the law.

Mashaal: Mashaal is a 1984 Bollywood film.  Produced and directed by Yash Chopra, it starred Dilip Kumar, Anil Kapoor, Waheeda Rehman, Rati Agnihotri, Nilu Phule, Iftekhar, Saeed Jaffery, Gulshan Grover, Alok Nath, Madan Puri and Amrish Puri.  The role played by Anil Kapoor was first offered to Amitabh Bachchan and then to Kamal Haasan, but after they declined the offer, the role went to Anil Kapoor.  Vinod Kumar (Dilip Kumar) plays a respected, law-abiding citizen who turns to crime for exacting revenge.

Saira Banu: Saira Banu (born 23 August 1944), also known as Saira Bano, is one of the most popular Indian Hindi film actresses and the wife of the film actor Dilip Kumar.  She acted in many Bollywood films between 1961 and 1988.

House of Dilip Kumar, Peshawar: House of Dilip Kumar, Peshawar housed the Indian film actor Dilip Kumar.  Born in Peshawar, British India on (1922--)11 1922 , Dilip Kumar relocated to Mumbai in the late 1930s with family.  It was named as a Pakistani national heritage monument on 13 July 2014 by the Pakistani Prime Minister Nawaz Sharif.

Question: When did Dilip Kumar's wife premier in Hamaari Beti Raaj Karegi?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "premiere_date": {
      "type": "string",
      "format": "date",
      "description": "The date when the series premiered."
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actress."
        },
        "relationship_to_dilip_kumar": {
          "type": "string",
          "description": "The relationship of the actress to Dilip Kumar."
        },
        "role_in_series": {
          "type": "string",
          "description": "Description of the actress's role in the series."
        }
      },
      "required": [
        "name",
        "relationship_to_dilip_kumar",
        "role_in_series"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "series_name",
    "premiere_date",
    "actress_details"
  ],
  "additionalProperties": false
}

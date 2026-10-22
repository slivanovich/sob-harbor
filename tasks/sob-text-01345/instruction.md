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
Bo Waterside: Bo Waterside is a town in Grand Cape Mount County, Liberia on the Mano River.  It was a key border crossing between Liberia and Sierra Leone until 1990, when it closed after the launch of Charles Taylor's National Patriotic Front of Liberia invasion from Sierra Leone.  The border crossing officially re-opened in June 2007 in an official ceremony involving government officials, humanitarian workers and significant amounts of foreign press coverage.

Mohamed Sillah: Mohamed Yahya Sillah was born December 12, 1949 in Massam Kpaka, Pujehun District, Republic of Sierra Leone.  His father, Alhaji Yahya Sillah, now 100 years old, served as Regent Chief (Acting Paramount Chief) for several years in Dama Chiefdom, Kenema District in the early seventies.  Alhaji Yahya Sillah was appointed to that high position by Sierra Leone President Siaka Stevens.  His mother, Haja Mamie Zoe Mansaray, was a home maker.  A journalist and human rights activist, Mohamed Yahya Sillah was a vocal torch-bearer in the transition efforts from military to civilian rule in Sierra Leone, 1996.  As Leader and National Chairman of National Alliance Democratic Party (NADP), he competed the 1996 Presidential elections in Sierra Leone, becoming one of only thirteen political leaders that qualified to contest the Presidential and Parliamentary elections in the country at the age of 46.  His adoring personality lured many Sierra Leoneans and media practitioners to view him as one of the most eloquent and charismatic politicians in Sierra Leone.  Nevertheless, he received only 0.5% of the votes (3,723 total votes), good for 13th place.  Although he protested the election results on BBC's Focus on Africa, he later suspended his protest "for the sake of peace."  Mohamed Yahya Sillah continues to enjoy massive support from the youth and women supporters in Sierra Leone.  In 2007, he withdrew his bid for national leadership in the Presidential and Parliamentary elections, citing inadequate funding and ineffective campaign management machinery.  He later put his weight behind the Sierra Leone Peoples Party (SLPP) presidential candidate, Vice President Solomon Berewa.  When Berewa lost the elections, Mohamed Yahya Sillah gracefully congratulated the winning candidate, Ernest Bai Koroma, of the All People's Congress (APC) party.  Mohamed Yahya Sillah vows to respect and help protect the dignity of any Sierra Leonean that is legitimately and democratically elected to office by the people of Sierra Leone.

United Nations Security Council Resolution 813: United Nations Security Council Resolution 813, adopted unanimously on 26 March 1993, after reaffirming Resolution 788 (1992) and determining that the situation in Liberia constituted a threat to international peace and security, the Council condemned the failure of the parties in the country – the Armed Forces of Liberia, ULIMO, National Patriotic Front of Liberia and Independent National Patriotic Front of Liberia among others, to implement the Yamoussoukro IV Accord.

Independent National Patriotic Front of Liberia: The Independent National Patriotic Front of Liberia (INPFL) was a rebel group that participated in the First Liberian Civil War under the leadership of Prince Johnson.  It was a breakaway faction of the National Patriotic Front of Liberia (NPFL).

Sierra Leone Civil War: The Sierra Leone Civil War (1991–2002) began on 23 March 1991 when the Revolutionary United Front (RUF), with support from the special forces of Charles Taylor’s National Patriotic Front of Liberia (NPFL), intervened in Sierra Leone in an attempt to overthrow the Joseph Momoh government.  The resulting civil war lasted 11 years, enveloped the country, and left over 50,000 dead.

Karamoh Kabba: Karamoh Kabba (born in 1965 in Koidu Town, Kono District, Sierra Leone) is a Sierra Leonean author, writer, novelist and journalist.  He has written several accounts about the Sierra Leone civil war, such as "A Mother’s Saga: An Account of the Rebel War in Sierra Leone" and the self-published work "Lion Mountain" and "Morquee: A Political Drama of Wish over Wisdom" published by Sierra Leone Writers Series.  He has published several short stories and verses of poems on the Web site, Sierra Leone Web.

John Leigh (ambassador): John Ernst Leigh was an Ambassador for Sierra Leone to the United States who served during the Sierra Leone Civil War.  Leigh was also a Presidential candidate for the Sierra Leone People's Party during the 2007 Presidential elections in Sierra Leone.

Sierra Leone's Refugee All Stars: Sierra Leone's Refugee All Stars (also called Refugee All Stars) is a band from Sierra Leone which was formed by a group of refugees displaced to Guinea during the Sierra Leone Civil War.  Since their return to Freetown in 2004, the band has toured extensively to raise awareness for humanitarian causes.  Their story is documented in the 2005 documentary film "Sierra Leone's Refugee All Stars".

Revolutionary United Front: Revolutionary United Front (RUF) was a rebel army that fought a failed eleven-year war in Sierra Leone, starting in 1991 and ending in 2002.  It later developed into a political party, which existed until 2007.  The three most senior surviving leaders, Issa Sesay, Morris Kallon and Augustine Gbao, were convicted in February 2009 of war crimes and crimes against humanity.

Special Court for Sierra Leone: The Special Court for Sierra Leone, or the "Special Court" (SCSL), also called the Sierra Leone Tribunal, was a judicial body set up by the government of Sierra Leone and the United Nations to "prosecute persons who bear the greatest responsibility for serious violations of international humanitarian law and Sierra Leonean law" committed in Sierra Leone after 30 November 1996 and during the Sierra Leone Civil War.  The court's working language was English.  The court listed offices in Freetown, The Hague, and New York City.

Question: Who fought the National Patriotic Front of Liberia in the Sierra Leone Civil War?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "conflict_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the civil conflict."
        },
        "start_year": {
          "type": "integer",
          "description": "The year the conflict began."
        },
        "end_year": {
          "type": "integer",
          "description": "The year the conflict ended."
        }
      },
      "required": [
        "name",
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    },
    "national_patriotic_front_of_liberia_involvement": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "description": "The role of the National Patriotic Front of Liberia in the conflict."
        },
        "allies": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Groups allied with the National Patriotic Front of Liberia."
        },
        "opponents": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Groups that fought against the National Patriotic Front of Liberia."
        }
      },
      "required": [
        "role",
        "allies",
        "opponents"
      ],
      "additionalProperties": false
    },
    "primary_question_answer": {
      "type": "string",
      "description": "The direct answer to who fought the National Patriotic Front of Liberia in the Sierra Leone Civil War."
    }
  },
  "required": [
    "conflict_details",
    "national_patriotic_front_of_liberia_involvement",
    "primary_question_answer"
  ],
  "additionalProperties": false
}

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
Bulhoek massacre: The Bulhoek massacre occurred on 24 May 1921, in the South African village of Bulhoek in the then Cape Province (today part of Eastern Cape).  After a dispute over land in Bulhoek, dating back to 1920, an 800-strong police force from the Union of South Africa and led by Colonel Johan Davey and General Koos van der Venter gathered at Ingxingwa Ye Nkunzini, in the Bulhoek valley, and Ingxingwa ka Stivini, Steven's Valley.  At the same time 500 men known as the "Israelites", armed with spears and knobkerries, and led by Enoch Mgijima, gathered in an open field, ready for battle.  After failed final negotiations between the two parties, a battled ensued.  The 20-minute battle, which left an estimated 163 Israelites dead, 129 wounded and 95 taken as prisoners, became known as the Bulhoek Massacre.

Leliefontein massacre: The Leliefontein massacre occurred at the Leliefontein mission station in the Northern Cape, South Africa on 31 January 1902.  Boer leader Manie Maritz executed 35 indigenous inhabitants of the settlement as punishment for attacking his party when he went to interview the European missionaries in the town during the Second Boer War.  Deneys Reitz described the attack as a "ruthless and unjustifiable act" and mentioned that Jan Smuts was displeased when he accompanied Reitz to the site of the massacre, afterward.

Leliefontein, Northern Cape: Leliefontein is a settlement in  Namakwa District Municipality in the Northern Cape province of South Africa.

Jacques Snyman: Jacques Snyman (born 10 May 1994) is a South African cricketer.  He was included in the Northern Cape squad for the 2016 Africa T20 Cup.  He made his Twenty20 (T20) debut for Northern Cape against South Western Districts on 16 September 2016.  He made his first-class debut for Northern Cape on 1 December 2016 in the 2016–17 Sunfoil 3-Day Cup.  He made his List A debut for Northern Cape on 17 December 2016 in the 2016–17 CSA Provincial One-Day Challenge.

Dipuo Peters: Elizabeth Dipuo Peters (born in Kimberley, Northern Cape on 13 May 1960) was the Minister of Transport of the Republic of South Africa (from 10 July 2013) until 30 March 2017, in the Zuma administration, and former Minister of Energy from 2009-2013 having served as successor to Manne Dipico as the second Premier of the Northern Cape Province, 22 April 2004 to 10 May 2009.  A member of the African National Congress (ANC), she serves on the Women's League National Executive Committee.  Dipuo Peters‚ has resigned as a member of parliament for the African National Congress.

John Block (South African politician): John Fikile Block (born 10 February 1968) was the Provincial Chairman of the African National Congress in the Northern Cape Province, South Africa, and was a Member of the Executive Council (MEC) for Finance, Economic Development and Tourism in the Northern Cape Provincial Government.  Block was found guilty of fraud, corruption and money laundering by the Northern Cape High Court in 2015.  In December 2016 he was sentenced to 15 years imprisonment.

Cloete Buitendag: Cloete Buitendag (born 18 May 1993) is a South African cricketer.  He was included in the Northern Cape squad for the 2016 Africa T20 Cup.  He made his first-class debut for Northern Cape in the 2016–17 Sunfoil 3-Day Cup on 20 October 2016.  He made his List A debut for Northern Cape in the 2016–17 CSA Provincial One-Day Challenge on 13 November 2016.

Sol Plaatje University: The Sol Plaatje University, which had provisionally been referred to as the University of the Northern Cape, opened in Kimberley, South Africa, in 2014, accommodating a modest initial intake of 135 students.  The student complement is expected to increase gradually towards a target of 7 500 students by 2024.  Launched in a ceremony in Kimberley on 19 September 2013, it had been formally established as a public university in terms of Section 20 of the Higher Education Act of 1997, by way of Government Notice 630, dated 22 August 2013.  Minister of Higher Education and Training, Blade Nzimande, observed at the launch that this “is the first new university (in South Africa) to be launched since 1994 and as such is a powerful symbol of the country’s democracy, inclusiveness, and growth.  It represents a new order of African intellect, with a firm focus on innovation and excellence."  Previously announcing the name for the university, on 25 July 2013, President Jacob Zuma mentioned the development of academic niche areas that did not exist elsewhere, or were under-represented, in South Africa.  "Given the rich heritage of Kimberley and the Northern Cape in general," Zuma said, "it is envisaged that Sol Plaatje will specialise in heritage studies, including interconnected academic fields such as museum management, archaeology, indigenous languages, and restoration architecture."

St. Mary's Cathedral, Kimberley: The St. Mary's Cathedral also called Catholic Cathedral of Kimberley Is the name given to a religious building affiliated with the  Roman Catholic Church which is located in 72 Du Toitspan of the city of Kimberley in the Northern Cape Province, part of the African country of South Africa.  It is dedicated to the Virgin Mary whom Christians believe is the Mother of God.

South Africa: South Africa, officially the Republic of South Africa (RSA), is the southernmost country in Africa.  It is bounded on the south by 2,798 km of coastline of Southern Africa stretching along the South Atlantic and Indian Oceans; on the north by the neighbouring countries of Namibia, Botswana, and Zimbabwe; and on the east and northeast by Mozambique and Swaziland; and surrounds the kingdom of Lesotho.  South Africa is the 25th-largest country in the world by land area, with close to 56 million people, is the world's 24th-most populous nation and the largest in Southern Africa.  It is the southernmost country on the mainland of the Old World or the Eastern Hemisphere.  About 80 percent of South Africans are of Sub-Saharan African ancestry, divided among a variety of ethnic groups speaking different Bantu languages, nine of which have official status.  The remaining population consists of Africa's largest communities of European (white), Asian (Indian), and multiracial (coloured) ancestry.

Question: In January of 1902, the Leliefontein massacre occurred in the Northern Cape of which African country that is home to 56 million people?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the African country where the massacre occurred."
    },
    "country_population": {
      "type": "integer",
      "description": "The approximate population of the country in millions."
    },
    "massacre_event": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the massacre event."
        },
        "date": {
          "type": "string",
          "description": "The date the massacre occurred."
        },
        "location_province": {
          "type": "string",
          "description": "The province within the country where the massacre took place."
        }
      },
      "required": [
        "name",
        "date",
        "location_province"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "country_name",
    "country_population",
    "massacre_event"
  ],
  "additionalProperties": false
}

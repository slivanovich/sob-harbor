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
Robert Guba Aisi: Robert Guba Aisi is the current Permanent Representative (ambassador) of Papua New Guinea to the United Nations in New York.  He presented his credentials to the Secretary General on June 25, 2002.  Prior to being appointed to the United Nations, Aisi was Councillor of Papua New Guinea’s Legal Training Institute.

Federico Cuello Camilo: Federico Alberto Cuello Camilo (Santo Domingo, 1966) is a diplomat of the Dominican Republic.  Since 14 July 2011, he is the Ambassador Extraordinary and Plenipotentiary to the United Kingdom of Great Britain and Northern Ireland.  Queen Elizabeth II received his credentials on 11 October 2011.  Previously, he served as the Permanent Representative of the Dominican Republic to the United Nations in New York, with the rank of Ambassador Extraordinary and Plenipotentiary from 3 June 2009 presented his letters of credence.  During his tenure in New York City the Dominican Republic was elected for the first time as member of the Executive Board of UN Women (2011–2014) and to the Economic and Social Council (ECOSOC, 2012–2013).  In December 2004, he was appointed ambassador extraordinary and plenipotentiary of the Dominican Republic to the Kingdom of Belgium, to the European Union, the Czech Republic, and Poland.  He was also the Dominican Ambassador, Permanent Representative to the European Office of the United Nations and to the World Trade Organization (WTO) in Geneva, Switzerland, between March 1999 and August 2002

Raimonda Murmokaitė: Raimonda Murmokaitė (born 17 July 1959) is a Lithuanian diplomat, serving as Permanent Representative of Lithuania to the United Nations since 25 October 2012, when she presented her credentials to UN Secretary-General Ban Ki-moon.  She served as President of the United Nations Security Council for February 2014 and May 2015.

Mohammad Khazaee: Mohammad Khazaee (Persian: محمد خزاعی‎ ‎ , born 12 April 1953 in Kashmar, Iran) is the former Ambassador of Iran to the United Nations.  He presented his credentials to the United Nations Secretary-General Ban Ki-moon in July 2007.  He was elected as Vice President of the United Nations General Assembly on 14 September 2011.

Japanese Peace Bell: The Japanese Peace Bell is a United Nations peace symbol.  Cast on November 24, 1952, it was an official gift of the Japanese people to the United Nations on June 8, 1954.  The symbolic bell of peace was donated by Japan to the United Nations at a time when Japan had not yet been officially admitted to the United Nations.  The Japanese Peace Bell was presented to the United Nations by the United Nations Association of Japan.

Kofi Annan: Kofi Atta Annan ( ; born 8 April 1938) is a Ghanaian diplomat who served as the seventh Secretary-General of the United Nations from January 1997 to December 2006.  Annan and the UN were the co-recipients of the 2001 Nobel Peace Prize.  He is the founder and chairman of the Kofi Annan Foundation, as well as chairman of The Elders, an international organization founded by Nelson Mandela.

Christopher Fitzherbert Hackett: Dr. Christopher Fitzherbert Hackett is the Permanent Representative for Barbados to the United Nations.  He presented his credentials to the Secretary-General of the United Nations on 12 March 2004.  During the 58th United Nations General Assembly, Hackett was a Senior Adviser to the President, Julian R. Hunte.

Jane Jimmy Chigiyal: Jane Jimmy Chigiyal (born April 3, 1967) is a Micronesian diplomat.  On October 4, 2011, Chigiyal was confirmed as the Permanent Representative to the United Nations in a 13-1 vote in the 17th session of the Congress of the Federated States of Micronesia.  Chigiyal's confirmation made her the first female Ambassador from the Federated States of Micronesia in history.  She presented her credentials to Secretary-General of the United Nations Ban Ki-moon on December 2, 2011.

Enrique Berruga: Enrique Berruga Filloy is a Mexican diplomat, having served as the Permanent Representative of Mexico to the United Nations.  He presented his credentials to United Nations Secretary-General Kofi Annan on December 16, 2003.  Prior to that, he had been an Undersecretary for Foreign Affairs from 2000 to 2003.  He has been a career diplomat since 1984, serving in positions such as the chief of staff of the Minister of Foreign Affairs in 1993 and from 1994 to 1997.  From 1997 to 1999, he was the Mexican ambassador to Costa Rica.

Rebecca Sommer: Rebecca Sommer is a German artist, journalist, photographer, documentary filmmaker, and a human rights, nature rights and climate justice activist.  She works with international NGO's in special consultative status to the United Nations (ECOSOC) in participatory status with the Council of Europe, and civil society observer status to the United Nations Framework Convention on Climate Change (UNFCCC).  She convened and co-founded in 2001 Earth Peoples in NYC, a global network working together to promote natural and human rights, with special focus on Indigenous Peoples, Climate Change and the Rights of Mother Earth.  2004 she was commissioned by the United Nations to film and produce the awareness-raising video "Indigenous Peoples and the United Nations Nr.1", which was first presented at the Dag Hammarskjöld Library Auditorium at the United Nations Headquarters.  In 2007, prior to the adoption of the United Nations Declaration on the Rights of Indigenous Peoples at the UN General Assembly, she created a video lobby-tool"Discussions on the UN Declaration on the Rights of Indigenous Peoples" to encourage discussions with a number of countries that expressed concern about some key issues, such as self-determination, access to lands, territories and resources and the lack of a clear definition of the term indigenous.  UN agencies UNHCHR and UNHCHR as well states such as Bolivia, Guatemala, Mexico and Germany supported her awareness-raising efforts and enabled during the year several film screenings of her work to encourage debates among states that were reluctant to adopt the Declaration.  Since 2013 she is the president of the Arbeitsgruppe Flucht+Menschenrechte (AG F+M), a network supporting refugees in Europe.

Question: Enrique Berruga presented his credentials to a united nations secertary-general from which country ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "diplomat": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the diplomat."
        },
        "role": {
          "type": "string",
          "description": "The role of the diplomat."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "secretary_general": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the UN Secretary-General."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country of origin of the UN Secretary-General."
        }
      },
      "required": [
        "name",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "credentials_presentation_date": {
      "type": "string",
      "description": "The date when the credentials were presented."
    }
  },
  "required": [
    "diplomat",
    "secretary_general"
  ],
  "additionalProperties": false
}

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
History of Jardine, Matheson &amp; Co.: Jardine Matheson & Co., later Jardine Matheson & Co.  Ltd., forerunner of today's Jardine Matheson Holdings, was a Far Eastern trading company founded in 1832 by Scotsmen William Jardine and James Matheson as senior partners.  Trading in opium, cotton, tea, silk and a variety of other goods, from its early beginnings in Canton (modern day Guangzhou), in 1844 the firm established its head office in the new British colony of Hong Kong then proceeded to expand all along the China Coast.

Charles Ives: Charles Edward Ives ( ; October 20, 1874May 19, 1954) was an American modernist composer.  He is one of the first American composers of international renown, though his music was largely ignored during his life, and many of his works went unperformed for many years.  Over time, he came to be regarded as an "American original".  He combined the American popular and church-music traditions of his youth with European art music, and was among the first composers to engage in a systematic program of experimental music, with musical techniques including polytonality, polyrhythm, tone clusters, aleatory elements, and quarter tones, foreshadowing many musical innovations of the 20th century.

HMS Curlew (1812): HMS "Curlew" (1812) was a Royal Navy "Cruizer" class brig-sloop built by (William) Good & Co., at Bridport and launched in 1812.  She served with the Navy for only 10 years.  During the War of 1812 she sailed from Halifax and captured several American privateers.  Her greatest moment was her role in the 1819 British occupation of Ras al-Khaimah.  "Curlew" was sold in 1822 in Bombay.  She then had a 13 or so year career as an opium runner for James Matheson, one of the founders of the firm Jardine Matheson.

Garynahine Estate: Garynahine Estate (Scottish Gaelic: "Gearraidh na h-aibhne" ) in Garynahine, a village on the Isle of Lewis, Outer Hebrides was owned by Sir James Matheson, born in Shiness, Lairg, Sutherland, Scotland, from 1844 to 1917.  He was the son of Captain Donald Matheson, a Scottish trader in India.

Arthur Matheson: Arthur James Matheson (December 1842 – January 25, 1913) was a Canadian lawyer and politician.  He served as a Conservative Member of the Legislative Assembly of Ontario for Lanark South from 1898 to 1913, and was provincial treasurer from 1905 to 1913.

Lews Castle: Lews Castle (Scottish Gaelic: "Caisteal Leòdhais") is a Victorian era castle located west of the town of Stornoway, Isle of Lewis, Scotland.  It was built in the years 1844-51 as a country house for Sir James Matheson who had bought the whole island a few years previously with his fortune from the Chinese Opium trade.  It was designed by the Glasgow architect Charles Wilson.

The Canton Register: The Canton Register was an English language newspaper founded by Scottish merchants James Matheson and his nephew Alexander together with Philadelphian William Wightman Wood, the first editor.  First published in Canton on November 8, 1827 and printed every two weeks, it was one of China's first English-language newspapers.

Elaine Morgan (singer): Elaine Morgan (born 1960, Cardiff) is a Welsh folk singer.  She was a member of Dan Ar Braz's group "L'Heritage des Celtes", and often sang lead vocals, either alone or jointly with Karen Matheson.  Morgan and Matheson received much acclaim for their performance on the Breton-language song "Diwanit Bugale", France's entry to the Eurovision Song Contest 1996.  Formed her own folk-rock band Rose among Thorns together with her husband Derek and produced several albums throughout the nineties.  Currently involved in the running of the Rumney Folk Club in Cardiff.  Has also worked with members of Fairport Convention and featured with them at their annual Cropredy gathering.

Jonathan B. Postel Service Award: The Jonathan B. Postel Service Award is an award named after Jon Postel.  The award has been presented every year since 1999 by the Internet Society to "honor a person who has made outstanding contributions in service to the data communications community."

James Matheson (composer): James Matheson (born 1970 in Des Moines, Iowa) is an American composer.  His works have been commissioned and performed by the Albany Symphony Orchestra, Chicago Symphony Orchestra, Los Angeles Philharmonic, New York Philharmonic, Borromeo String Quartet, Carnegie Hall and the St. Lawrence String Quartet.  In December 2011, he received the Charles Ives Living from the American Academy of Arts and Letters, an award providing him with $100,000 for two years (2012-2014).  Previously, he received the Academy’s Goddard Lieberson Fellowship in 2008 and Hinrichsen Award in 2002.  He has also received awards from the Civitella Ranieri, Bogliasco and Sage Foundations, ASCAP, and the Robbins Prize.  He was executive director of the MATA Festival of New Music in New York from 2005-2007 and has been a fellow at the Aspen Music Festival.  Since September 2009, he has been the director of the Los Angeles Philharmonic’s Composer Fellowship Program.

Question: What year did the person James Matheson received an award named for in 2011 die?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_recipient_name": {
      "type": "string",
      "description": "The name of the person who received the award."
    },
    "award_year_received": {
      "type": "integer",
      "description": "The year the award was received."
    },
    "award_name": {
      "type": "string",
      "description": "The name of the award received."
    },
    "person_award_is_named_after": {
      "type": "string",
      "description": "The name of the person after whom the award is named."
    },
    "death_year_of_named_person": {
      "type": "integer",
      "description": "The year the person after whom the award is named died."
    }
  },
  "required": [
    "award_recipient_name",
    "award_year_received",
    "award_name",
    "person_award_is_named_after",
    "death_year_of_named_person"
  ],
  "additionalProperties": false
}

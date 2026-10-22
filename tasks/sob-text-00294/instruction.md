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
Louisa Stanhope: Louisa Sidney Stanhope (fl.  1806–1827) was an English novelist of the early 19th century.  She wrote mainly historical and Gothic romances, in great profusion, counting as the tenth most productive novelist in Britain in the period 1800 to 1829.  Her didactic novels were aimed mainly at younger female readers.

Today's Housewife: Today's Housewife was an American women's magazine in the early 20th century.

Pucchigumi: Pucchigumi (ぷっちぐみ , Putchigumi ) is a Japanese monthly children's manga magazine published by Shogakukan.  Several different manga titles, and adaptations aimed at young female readers have been serialized in the magazine in its decade long history.  The latest circulation figures places the magazine at 68,333 copies which is around the middle of the circulation list when compared to other manga magazines.

Demet (magazine): The Ottoman women's magazine Demet ("floral bouquet") was founded in 1908 in Istanbul, two weeks after the proclamation of the Second Constitutional Era.  Altogether, seven issues exist, they were published once a week.  Editor-in-chief and publisher was Celāl Sāhir (1883–1935).  Even though the magazine was aimed at women, the editorial team of the first two issues was made up exclusively of men, such as Mehmet Akif Ersoy (1873–1936), Selim Sırrı (Tarcan) (1874–1957), and Enis Avni (1886-1958).  Among the female writers were later Halide Salih Hanımlar (Halide Edip, 1884–1964), Nigar Bint-i Osman (1862–1918), and İsmet Hakkı Hanım.  In addition to literary and scientific articles, what interested the female readers most were political publications.  Besides Kadınlar Dünyası (1913–1921), Maḥāsin (1908–1910), and Kadın (1908–1910), is considered one of the first and most important women's magazines in the Second Constitutional Era.

Stellar (magazine): Stellar Magazine (stylised as STELLAR MAGAZINE) is a glossy Irish lifestyle and fashion magazine targeted at female readers in the age group of eighteen to thirty-four.  It is part of the VIP publishing franchise of Michael O'Doherty.  "Stellar" was launched on 15 October 2008 as the second of O'Doherty's solo business ventures, following the publication of the teenage-oriented advice magazine "Kiss" which was launched on 31 October 2002.  O'Doherty had previously engaged in a number of co-ordinated business ventures in Ireland with his former business partner John Ryan; "Stellar" succeeded the co-owned establishments of "Magill" in 1997 and "VIP" in 1999 and preceded later titles such as the unsuccessful "New York Dog" magazine which was based in New York City and aimed at the city's animal lovers.  "Stellar"'s chief rivals are the "Irish Tatler" and "Image".

Aurora Publishing (United States): Aurora Publishing, Inc. was the American subsidiary of Japanese publisher Ohzora Publishing, the leading "josei" manga publisher in Japan.  Headquartered in Torrance, California, it licensed and published Japanese manga for the North American market.  Aurora Publishing's first release was "Walkin' Butterfly" under the "shōjo" imprint "Aurora", which features manga targeting female readers in their teens and younger.  Aurora Publishing also released manga under two other imprints: the "yaoi" imprint "Deux Press" featured female-oriented manga about homoerotic relations between beautiful men, while the "josei" imprint "Luv Luv" featured erotic romance manga targeting female readers in their late teens and up.  Aurora Publishing distributed some of its manga via Netcomics.  In 2010, the Aurora office in California closed.  The former employees of Aurora Publishing went on to found Manga Factory.  Manga Factory lasted until at least June, 2013 before it closed as well.

Me Naiset: Me Naiset (meaning "We the Women" in English) is a Finnish language women's magazine published in Helsinki, Finland.  It is one of the largest weekly women's magazines in the country.

Arthur's Lady's Home Magazine: Arthur's Home Magazine (1852-ca.1898) or Ladies' Home Magazine was an American periodical published in Philadelphia by Timothy Shay Arthur.  Editors Arthur and Virginia Francis Townsend selected writing and illustrations intended to appeal to female readers.  Among the contributors: Mary Tyler Peabody Mann and Kate Sutherland.  In its early years the monthly comprised a selection of articles originally published in Arthur's weekly "Home Gazette."  Its nonfiction stories contained occasional factual inaccuracies for the sake of a good read.  A contemporary review judged it "gotten up in good taste and well; and is in nothing overdone.  Even its fashion plates are not quite such extravagant caricatures of rag-baby work as are usually met with in some of the more fancy magazines."  Readers included patrons of the Mercantile Library Association of San Francisco.

Matron literature: Matron literature (also known as hen lit) is a literary genre which focuses on older female characters as protagonists.  The genre has increased in popularity as the baby boomers have aged and female readers have sought characters to identify with.  Subjects are often romantic in nature, and heroines are usually between the ages of 45 and 65.  Matron lit characters were often married at one point, but are no longer with their spouses or living with their children.  There are usually feminist themes in matron literature, though some works are more overtly feminist than others.

Fanny Fern: Fanny Fern, born Sara Willis (July 9, 1811 – October 10, 1872), was an American newspaper columnist, humorist, novelist, and author of children's stories in the 1850s-1870s.  Fern's great popularity has been attributed to her conversational style and sense of what mattered to her mostly middle-class female readers.  By 1855, Fern was the highest-paid columnist in the United States, commanding $100 per week for her "New York Ledger" column.

Question: Are the magazines, Me Naiset and Today's Housewife, catering to female readers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_answered": {
      "type": "boolean",
      "description": "Indicates whether the question about the magazines catering to female readers could be answered from the context."
    },
    "all_magazines_cater_to_female_readers": {
      "type": "boolean",
      "description": "True if all listed magazines cater to female readers, false otherwise."
    },
    "magazines_details": {
      "type": "array",
      "description": "Details for each magazine mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "magazine_name": {
            "type": "string",
            "description": "The name of the magazine."
          },
          "target_audience_confirmed_female": {
            "type": "boolean",
            "description": "True if the context confirms the magazine targets female readers."
          },
          "evidence": {
            "type": "string",
            "description": "The specific text from the context supporting the target audience."
          }
        },
        "required": [
          "magazine_name",
          "target_audience_confirmed_female",
          "evidence"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_answered",
    "all_magazines_cater_to_female_readers",
    "magazines_details"
  ],
  "additionalProperties": false
}

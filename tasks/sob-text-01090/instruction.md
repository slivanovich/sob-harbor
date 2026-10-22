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
Ananga Ranga: The Ananga Ranga (अनंगरंग "Stage of Love") or Kamaledhiplava (कमलेधिप्लव "Boat in the Sea of Love") is an Indian sex manual written by Kalyana malla in the 15th or 16th century.  The poet wrote the work in honor of Lad Khan, son of Ahmed Khan Lodi.  He was related to the Lodi dynasty, which from 1451 to 1526 ruled from Delhi.  Later commentators have said it is aimed specifically at preventing the separation of a husband and wife.  This work is often compared to the "Kama Sutra", on which it draws.

Henry Miller: Henry Valentine Miller (December 26, 1891 – June 7, 1980) was an American writer, expatriated in Paris at his flourishing.  He was known for breaking with existing literary forms, developing a new sort of semi-autobiographical novel that blended character study, social criticism, philosophical reflection, explicit language, sex, surrealist free association, and mysticism.  His most characteristic works of this kind are "Tropic of Capricorn", The Colossus of Maroussi, The Time of the Assassins, and "The Books in My Life", many of which are based on his experiences in New York and Paris (some of which were banned in the United States until 1961), adding Big Sur and the Oranges of Heronymous Bosch while finally residing in Big Sur, California.  He also wrote travel memoirs and literary criticism, and painted watercolors.

Thomas James (bishop): John Thomas James (1786 – 1828) was a Church of England bishop.  He was bishop of Calcutta from 1827 to 1828.  He also wrote travel and art books.

The Westminster Gazette: The Westminster Gazette was an influential Liberal newspaper based in London.  It was known for publishing sketches and short stories, including early works by Raymond Chandler, Anthony Hope, D. H. Lawrence, Katherine Mansfield, and Saki, and travel writing by Rupert Brooke.  One of its editors was caricaturist and political cartoonist Francis Carruthers Gould.

Ivan Ivanić: Ivan Ivanić (Bačko Gradište, Bečej, Austria-Hungary, April 24, 1867 – Belgrade, Kingdom of Yugoslavia, January 31, 1935) was a diplomat of the Kingdom of Serbia and author of numerous works about ethnic groups in Serbia and the Balkans.  He also wrote travel literature which described his travels in the region of Old Serbia (especially Kosovo and Metohija and Macedonia).

Shin Maha Silavamsa: Shin Maha Silavamsa(Burmese: ရှင်မဟာ သီလဝံသ ) is a Theravadan Buddhist monk who lived Ava Kingdom (1364–1555) of Myanmar.  He is famous for his poetry and he is one of the greatest poets of ancient Burma.  Paramitawkhan Pyoပါရမီတော်ခန်းပျို့ and Sautaungkhan Pyoဆိုတောင်းခန်းပျို့ are his masterpieces.  Those are religious poetry and so deep to understand for ordinary people who don't have proper Buddhism knowledge.  In ancient Myanmar, poet wrote poetry base on three subjects, about the world(the living environment)လောကအရေး , about the Kingsရာဇအရေး and about the Dharma(Religions)ဓမ္မအရေး .  Shin Maha Silavamsa focused on religious poetry.

Bernard Newman (author): Bernard Charles Newman (8 May 1897 – 19 February 1968) was a British author of over 100 books, both fiction and non-fiction.  An historian, he was considered an authority on spies, but also wrote travel books and on politics.  His fiction included mystery novels, science fiction and children's books.

Rupert Brooke: Rupert Chawner Brooke (middle name sometimes given as "Chaucer"; 3 August 1887 – 23 April 1915) was an English poet known for his idealistic war sonnets written during the First World War, especially "The Soldier".  He was also known for his boyish good looks, which were said to have prompted the Irish poet W. B. Yeats to describe him as "the handsomest young man in England".

Daphne Rooke: Daphne Marie Rooke (née Pizzey) (6 March 1914 – 21 January 2009 ) was a South African author of works such as "Mittee", "Ratoons" and "Wizards' Country".  She also wrote travel articles and books for children set in India, Australia, New Zealand, and South Africa.

Dance in Uzbekistan: Uzbekistan Dance consists of between 15-20 thousand movements by a performer, depending on the complexity of the dance. [citation needed]. An Uzbek dance portrays a story, told by the flowing movements and rhythm.  The lithe and expressive hands of a dancer raise and then interweave like two twigs of an almond tree, then one hand is above the head and the other is making swift movements around the body.  A medieval poet wrote: "A dancing women!  She is swiftly dancing, spinning like snow carried away by a whirlwind.  Restless, she is spinning to the left and to the right". [citation needed]

Question: Which English poet wrote travel 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "poet_name": {
      "type": "string",
      "description": "The full name of the poet."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the poet."
    },
    "known_for_works": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of literary forms or specific works the poet is known for."
    },
    "wrote_travel_literature": {
      "type": "boolean",
      "description": "Indicates if the poet wrote travel literature."
    }
  },
  "required": [
    "poet_name",
    "nationality",
    "known_for_works",
    "wrote_travel_literature"
  ],
  "additionalProperties": false
}

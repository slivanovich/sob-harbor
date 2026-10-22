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
Winnie George: Winifred Una Margaretta George (born 19 January 1914 in Mordialloc, Victoria, Australia - died 19 March 1988 in Dandenong, Victoria) was an Australian cricket player.  George played three tests for the Australia national women's cricket team.  George was the sixteenth woman to play Women's Test cricket for Australia.

Ehyophsta: Ehyophsta (Cheyenne for "Yellow-Haired Woman") was a Cheyenne woman.  She was the daughter of Stands-in-the-Timber who died in 1849, and she was the niece of Bad Faced Bull.  She fought in the Battle of Beecher Island in 1868, and also fought the Shoshone that same year, where she counted coup against one enemy and killed another.  She fought the Shoshone again in 1869.  She was also a member of a secret society composed exclusively of Cheyenne women.  She died in 1915.

Navadurga (regional goddess): Navadurga is the Kuldevta (family deity) of many Gaud Saraswat Brahmins (GSB's) and Daivadnya Brahmins in India - in Goa & Maharashtra.  Due to the forceful Portuguese conversion and intervention into their rituals, the Deity with all the other purushas had to be shifted from Gavasim to their present respective places.  The Saraswats and Daivadnyas who left to the north of Goa, established a temple in the honours of the Goddess.  The present temple along with the kulpurushas is located in Vengulara Redi(Maharashtra).  The other Saraswats and Daivadnyas who left to the East of Goa along with their Kulapurushas established a temple dedicated to the Goddess.  Today the magnificent temple located in Madkai, is famous for its Navadurga having a tilted head.  Legend says that a wealthy Saraswat merchant when placed a flower worth Rs. 1000, the Goddess tilted her head acknowledging the merchant's devotion.  A similar legend follows at the Katyayani Baneshwar, a Konkani temple (once located in Benaulim, Goa) now located in Aversa, Karnataka.  Here Katyayani too like the Navadurga has a tilted head.As the legend goes a goldsmith belonging to Daivadnya Brahmin community living in the village of Madkai was ordered by temple authorities to fabricate a mask of the Goddess Navdurga.  The Goddess appeared in the goldsmith’s dream and told him to make the mask similar to his daughter’s face.  The mask was prepared resembling his daughter’s face, but after few days his daughter became weak and died.  The goldsmith was very sad because of her death.  The Goddess appeared before him once again and told him that she will visit his house once in a year as his daughter.  Hence as a tradition goes the same mask of the Goddess is welcomed in the Goldsmith’s house on Karthik Shukla Asthami day every year.  This day is celebrated by the Madkaikars(Goldsmith's family) in the same way as a married girl visiting her paternal home.  The Navdurgas located in Madkai (Goa), Kundaim (Goa) and Redi (Vengurla - Maharashtra) are considered to be Saraswat Kuldevtas whereas the others are gram devtas or normal Hindu temples.

Betty Hemings: Elizabeth "Betty" Hemings ( 1735 – 1807) was an enslaved mixed-race woman in colonial Virginia.  She had six children with her master, planter John Wayles, over a 12-year period, including Sally Hemings; they were three-quarters white and, following the condition of their mother, all were enslaved from birth and half-siblings to his daughter Martha Jefferson.  After Wayles died, the Hemings family and some 120 other slaves were inherited, along with 11,000 acres and £4,000 debt as part of his estate by his daughter Martha and her husband Thomas Jefferson.

Martha Broissier: Martha Broissier (born 1556, died after 1578), was a French woman who was made famous around the year of 1578 for her feigned demonic possession at the age of 22.  A fraud that was discovered by bishop Charles Miron, of which is either a Roman Catholic Diocese of Angers or a Roman Catholic Diocese of Orléans.  According to Augustin Calmet, Martha was young woman and daughter of a weaver in Romorantin.  She claimed to have been demonically possessed creating widespread circulation of the news in her time.  Martha's case of demonic possession is often used by ancient theological historians in comparison with the Loudun possessions since both cases consist of convincing accounts of demonic possession yet are presumed to have been historically fraudulent affairs that reached the peak of fame.

Ann Eliza Bleecker: Ann Eliza Bleecker (October 1752 – November 23, 1783) was an American poet and correspondent.  Following a New York upbringing, Bleecker married John James Bleecker, a New Rochelle lawyer, in 1769.  He encouraged her writings, and helped her publish a periodical containing her works.

Jacob Dissius: Jacob Abrahamsz.  Dissius (1653 - 1695) was a Dutch typographer and printer.  He is most notable as an art collector and for his links to Johannes Vermeer - his collection included 21 Vermeer works (including "The Milkmaid", "Portrait of a Young Woman", "A Girl Asleep", "Woman Holding a Balance" and "The Music Lesson") and in 1680 he married Madgdalene, daughter and sole heir of Vermeer's main patron Pieter van Ruijven.  Dissius died in 1695 and his collection was auctioned off in Amsterdam the following year.

Nicnevin: Nicneven or Nicnevin or Nicnevan (whose name is from a Scottish Gaelic surname, Neachneohain meaning "daughter(s) of the divine" and/or "daughter(s) of Scathach" NicNaoimhein meaning "daughter of the little saint") is a Queen of the Fairies in Scottish folklore.  In Ireland and Scotland, "the Feile na Marbh", (the “festival of the dead”) took place on Samhain (Celtic New Year) The names Satia, NICNEVEN, Bensozie, Zobiana, Abundia, Herodiana, were all used to identify the Scottish Witch Goddess of Samhain.  The use of the name for this meaning was first found in Montgomerie’s Flyting (c.1585) and was seemingly taken from a woman in Scotland condemned to death for witchcraft before being burnt at the stake as a witch.  In the Borders the name for this archetype was Gyre-Carling whose name had variants such as Gyre-Carlin, Gy-Carling, Gay-Carlin amongst others.  "Gyre" is possibly a cognate of the Norse word "geri" and thus having the meaning of "greedy" or it may be from the Norse "gýgr" meaning "ogress"; "carling" or "carline" is a Scots and Northern English word meaning "old woman" which is from, or related to, the Norse word "kerling" (of the same meaning).

Margaretta Faugères: Margaretta Bleecker Faugères (October 11, 1771 – January 9, 1801) was the daughter of Ann Eliza Bleecker.  She was an American playwright, poet and political activist.

Theodore de Lemos: Theodore de Lemos (1850, Holstein, German Confederation – 12 April 1909, New York City, New York, United States), son of Hermann and Maria Grothe De Lemos of Holstein, was an architect.  He graduated with honors from the Berlin Royal Academy of Buildings, and was famous for his designs in three countries, Germany, Mexico, and the United States.  In 1881, de Lemos left Germany and settled in New York, where he married Margaretta Becker and had a daughter, Marie Katherine.  He died in April, 1909, and is interred at Woodlawn Cemetery in The Bronx, New York City.

Question: Margaretta Faugères is the daughter of a woman that died in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "daughter_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the daughter."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the daughter."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the daughter."
        }
      },
      "required": [
        "name",
        "birth_year",
        "death_year"
      ],
      "additionalProperties": false
    },
    "mother_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the mother."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the mother."
        }
      },
      "required": [
        "name",
        "death_year"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string",
      "description": "Describes the relationship between the daughter and the mother."
    }
  },
  "required": [
    "daughter_info",
    "mother_info",
    "relationship_type"
  ],
  "additionalProperties": false
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMichelle Dockery: Michelle Suzanne Dockery (born 15 December 1981) is an English actress and singer.  She is most widely known for her performance as Lady Mary Crawley in the ITV (UK) and PBS (U.S.) television period drama series \"Downton Abbey\" (2010–15), for which she was nominated for three consecutive Emmy Awards in the category for Outstanding Lead Actress In Drama Series, and a Golden Globe Award nomination.  She made her professional stage debut in \"His Dark Materials\" in 2004.  For her role as Eliza Doolittle in the 2007 London revival of \"Pygmalion\", she was nominated for the Evening Standard Award.\n\nLabyrinth (miniseries): Labyrinth is a historical television miniseries based on the 2005 novel of the same name by Kate Mosse.  The setting jumps between modern and medieval France and follows two women (played by Vanessa Kirby and Jessica Brown Findlay) who are searching for the Holy Grail.  Other cast members include Katie McGrath, Tom Felton, Sebastian Stan, Emun Elliott, Tony Curran, and John Hurt.  Adrian Hodges adapted the novel for the series, which was directed by Christopher Smith.\n\nJessica (miniseries): Jessica is an Australian television miniseries based on the historical novel by Bryce Courtenay.  Originally broadcast by Australia's Network Ten in 2004 and set in the Australian outback at the turn of the twentieth century, this family based drama follows a young woman who is unjustly institutionalised.  Jessica won a 2005 Logie award for best mini-series or telemovie, plus two awards at the 2004 Chicago International Film Festival - one of them for the direction of Australian Peter Andrikidis.\n\nList of Baileys Women's Prize for Fiction winners: The Baileys Women's Prize for Fiction (previously called Women's Prize for Fiction (2013), Orange Prize for Fiction (1996–2006 & 2009–12) and Orange Broadband Prize for Fiction (2007–2008)) is one of the United Kingdom's most prestigious literary prizes, annually awarded to a female author of any nationality for the best original full-length novel written in English, and published in the United Kingdom in the preceding year.  The prize was originally due to be launched in 1994 with the support of Mitsubishi but public controversy over the merits of the award caused the sponsorship to be withdrawn.  Funding from Orange, a UK mobile network operator and Internet service provider, allowed the prize to be launched in 1996 by a committee of male and female \"journalists, reviewers, agents, publishers, librarians, booksellers\", including current Honorary Director Kate Mosse.\n\nLaura Carmichael: Laura Elizabeth Carmichael (born 16 July 1986) is an English actress, most widely known for her performance as Lady Edith Crawley in the ITV (UK) and PBS (U.S.) television period drama series\" Downton Abbey\".  Her other television work includes \"Marcella\" (2016). , and the feature film \"A United Kingdom\" (2016).\n\nLabyrinth (novel): Labyrinth is an archaeological mystery English-language novel written by Kate Mosse set both in the Middle Ages and present-day France.  It was published in 2005.\n\nKate Mosse: Katharine Louise Mosse OBE (born 20 October 1961), or Kate Mosse, is an English novelist, non-fiction and short story writer and broadcaster.  She is best known for her 2005 novel \"Labyrinth\", which has been translated into more than 37 languages.\n\nJane Wymark: Jane Wymark (born 31 October 1952) is an English actress.  The daughter of English actor Patrick Wymark (1926–1970) and the American writer and playwright Olwen Wymark, she is best known for playing Morwenna Chynoweth Whitworth (Morwenna Carne by the close of the series) in the 1970s BBC television period drama \"Poldark\" (1977), and more recently as Joyce Barnaby (1997–2011) in the ITV detective series \"Midsomer Murders\".  She has appeared in UK television dramas such as \"The Bass Player and the Blonde\", \"A Touch of Frost\", \"Dangerfield\", \"Lovejoy\" and \"Pie in the Sky\".  She also appeared as Jill Mason in the Birmingham Rep production of \"Equus\".\n\nSepulchre (Mosse novel): Sepulchre is a novel by the English author Kate Mosse.  The story is based in two time periods, 1891 and present day (2007), and follows two female protagonists.  It was published in 2007.\n\nJessica Brown Findlay: Jessica Rose Brown Findlay (born 13 September 1989) is an English actress, most widely known for her performance as Lady Sybil Crawley in the ITV (UK) and PBS (U.S.) television period drama series\" Downton Abbey\", and for her role as Emelia Conan Doyle in the 2011 British comedy-drama feature film \"Albatross\".\n\nQuestion: Labyrinth is a historical television miniseries based on the 2005 novel of the same name by Kate Mosse, the setting jumps between modern and medieval France, and follows two women, one being Jessica Rose Brown Findlay (born 13 September 1989) is an English actress, most widely known for her performance as Lady Sybil Crawley in which ITV (UK) and PBS (U.S.) television period drama series?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"miniseries_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the miniseries mentioned in the question.\"\n    },\n    \"miniseries_novel_author\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the novel on which the miniseries is based.\"\n    },\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the actress.\"\n        },\n        \"role_in_known_series\": {\n          \"type\": \"string\",\n          \"description\": \"The character role the actress is known for in the specified series.\"\n        },\n        \"known_for_series_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the television series the actress is most widely known for.\"\n        },\n        \"known_for_series_broadcasters\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The broadcasters of the television series the actress is known for.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_known_series\",\n        \"known_for_series_title\",\n        \"known_for_series_broadcasters\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"miniseries_title\",\n    \"miniseries_novel_author\",\n    \"actress_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "miniseries_title": {
        "type": "string",
        "description": "The title of the miniseries mentioned in the question."
      },
      "miniseries_novel_author": {
        "type": "string",
        "description": "The author of the novel on which the miniseries is based."
      },
      "actress_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the actress."
          },
          "role_in_known_series": {
            "type": "string",
            "description": "The character role the actress is known for in the specified series."
          },
          "known_for_series_title": {
            "type": "string",
            "description": "The title of the television series the actress is most widely known for."
          },
          "known_for_series_broadcasters": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The broadcasters of the television series the actress is known for."
          }
        },
        "required": [
          "name",
          "role_in_known_series",
          "known_for_series_title",
          "known_for_series_broadcasters"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "miniseries_title",
      "miniseries_novel_author",
      "actress_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

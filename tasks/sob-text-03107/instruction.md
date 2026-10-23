{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Tyger: \"The Tyger\" is a poem by the English poet William Blake published in 1794 as part of the \"Songs of Experience\" collection.  Literary critic Alfred Kazin calls it \"the most famous of his poems\", and \"The Cambridge Companion to William Blake\" says it is \"the most anthologized poem in English\".  It is one of Blake's most reinterpreted and arranged works.\n\nAuguries of Innocence (poetry collection): Auguries of Innocence is a poetry collection by Patti Smith, published in 2005.  This collection of poetry includes exactly twenty-six recent poems penned by the active, contemporary poet.  Drawing on some of her many influences such as William Blake and Arthur Rimbaud, Smith's collection here demonstrates over and over again her knack for detail.  Obviously William Blake is a dominant influence on the poet herself, since it shares its title, Auguries of Innocence, with one of William Blake's poems.  Upon reviewing both collections it is clearly obvious that both collections share more commonalities than just similar titles.  One commonality between this collection and that by Blake's, in regard to the content, is that the poems collected here exhibit subtle nods to Blake.  For example, in one of her poems, \"The Long Road\", by the end of the very first verse the reader has already been exposed to such suggestive visuals as the speaker of the poem sleeping in chimneys and chewing on bulbs, as well as the speaker \"sweeping time\".  Such visuals of Smith's conjure up recollections in the seasoned and experienced reader's mind of Blake's \"The Chimney Sweeper\" and \"The Blossom\".  While the majority of the twenty-six collected poems have some type of stanza-like arrangement the poet also incorporates several free-verse style poems into the collection, such as Mummer Love, Eve of All Saints, Our Jargon Muffles The Drum, and Written By A Lake.\n\nFearful Symmetry (Frye): Fearful Symmetry: A Study of William Blake is a 1947 book by Canadian literary critic Northrop Frye whose subject is the work of English poet and visual artist William Blake.  The book has been hailed as one of the most important contributions to the study of William Blake and one of the very first that embarked on the interpretation of many of Blake's most obscure works.  As Frye himself acknowledges, Blake's work is not to be deciphered but interpreted and seen within its specific historical and social contexts.\n\nPoetical Sketches: Poetical Sketches is the first collection of poetry and prose by William Blake, written between 1769 and 1777.  Forty copies were printed in 1783 with the help of Blake's friends, the artist John Flaxman and the Reverend Anthony Stephen Mathew, at the request of his wife Harriet Mathew.  The book was never published for the public, with copies instead given as gifts to friends of the author and other interested parties.  Of the forty copies, fourteen were accounted for at the time of Geoffrey Keynes' census in 1921.  A further eight copies had been discovered by the time of Keynes' \"The Complete Writings of William Blake\" in 1957.  In March 2011, a previously unrecorded copy was sold at auction in London for £72,000.\n\nBlake Edwards: Blake Edwards (born William Blake Crump; July 26, 1922 – December 15, 2010) was an American film director, screenwriter, and producer.\n\nStrangler of the Swamp: Strangler of the Swamp is a 1946 American horror film, produced and distributed by Producers Releasing Corporation.  It was written and directed by Frank Wisbar, and stars Rosemary LaPlanche, Robert Barrat and Blake Edwards.  It is a remake of Wisbar's earlier German film \"Fährmann Maria\" (1936).\n\nWitness Against the Beast: Witness Against the Beast: William Blake and the Moral Law is a 1993 book by the British historian E. P. Thompson in which Thompson contextualizes the work of the otherwise enigmatic poet and painter William Blake.  The last book that Thompson would write, it was published posthumously.  The book attempts to frame some of Blake's ideas in the traditions of the culture of religious dissent in England.\n\nLife of William Blake: The Life of William Blake, “Pictor Ignotus.”  With selections from his poems and other writings is a two volume work on the English painter and poet William Blake, first published in 1863.  The first volume is a biography and the second a compilation of Blake's poetry, prose, artwork and illustrated manuscript.\n\nThe Ancient of Days: The Ancient of Days is a design by William Blake, originally published as the frontispiece to a 1794 work, \"Europe a Prophecy\".  It draws its name from one of God's titles in the Book of Daniel and shows Urizen crouching in a circular design with a cloud-like background.  His outstretched hand holds a compass over the darker void below.  Related imagery appears in Blake's \"Newton\", completed the next year.  As noted in Gilchrist's \"Life of William Blake\", the design of \"The Ancient of Days\" was \"a singular favourite with Blake and as one it was always a happiness to him to copy.\"  As such there are many versions of the work extant, including one completed for Frederick Tatham only weeks before Blake's death.\n\nTiriel (poem): Tiriel is a narrative poem by William Blake, written \"c.\"1789.  Considered the first of his prophetic books, it is also the first poem in which Blake used free septenaries, which he would go on to use in much of his later verse.  \"Tiriel\" was unpublished during Blake's lifetime and remained so until 1874, when it appeared in William Michael Rossetti's \"Poetical Works of William Blake\".  Although Blake did not engrave the poem, he did make twelve sepia drawings to accompany the rough and unfinished manuscript, although three of them are considered lost as they have not been traced since 1863.\n\nQuestion: William Blake Crump directed a movie which was a remake of what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film that was a remake.\"\n    },\n    \"original_film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the original film that the specified movie was a remake of.\"\n    },\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person mentioned in the question.\"\n    },\n    \"person_role_in_film\": {\n      \"type\": \"string\",\n      \"description\": \"The actual role of the person in the film, as per the context.\"\n    },\n    \"remake_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the remake film.\"\n    },\n    \"original_film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The publication year of the original film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"original_film_title\",\n    \"person_name\",\n    \"person_role_in_film\",\n    \"remake_director\",\n    \"original_film_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film that was a remake."
      },
      "original_film_title": {
        "type": "string",
        "description": "The title of the original film that the specified movie was a remake of."
      },
      "person_name": {
        "type": "string",
        "description": "The name of the person mentioned in the question."
      },
      "person_role_in_film": {
        "type": "string",
        "description": "The actual role of the person in the film, as per the context."
      },
      "remake_director": {
        "type": "string",
        "description": "The director of the remake film."
      },
      "original_film_year": {
        "type": "integer",
        "description": "The publication year of the original film."
      }
    },
    "required": [
      "film_title",
      "original_film_title",
      "person_name",
      "person_role_in_film",
      "remake_director",
      "original_film_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDramatic Lyrics: Dramatic Lyrics is a collection of English poems by Robert Browning, first published in 1842 as the third volume in a series of self-published books entitled \"Bells and Pomegranates\".  It is most famous as the first appearance of Browning's poem \"The Pied Piper of Hamelin\", but also contains several of the poet's other best-known pieces, including \"My Last Duchess\", \"Soliloquy of the Spanish Cloister\", \"Porphyria's Lover\", and \"Johannes Agricola in Meditation\".\n\nShe dwelt among the untrodden ways: \"She Dwelt among the Untrodden Ways\" is a three-stanza poem written by the English Romantic poet William Wordsworth in 1798 when he was 28 years old.  The verse was first printed in \"Lyrical Ballads\", 1800, a volume of Wordsworth's and Samuel Taylor Coleridge's poems that marked a climacteric in the English Romantic movement.  The poem is the best known of Wordsworth's series of five works which comprise his \"Lucy\" series, and was a favourite amongst early readers.  It was composed both as a meditation on his own feelings of loneliness and loss, and as an ode to the beauty and dignity of an idealised woman who lived unnoticed by all others except by the poet himself.  The title line implies Lucy lived unknown and remote, both physically and intellectually.  The poet's subject's isolated sensitivity expresses a characteristic aspect of Romantic expectations of the human, and especially of the poet's, condition.\n\nMatthew Mead (poet): Matthew Mead (born 1924, Buckinghamshire, died 2009) was an English poet as well as a translator, with his wife Ruth, of German poets, including Johannes Bobrowski and Nelly Sachs.  He edited the magazine \"Satis\" and lived in Germany.  A selection of his poems appears in \"Penguin Modern Poets 16\", together with Harry Guest and Jack Beeching.\n\nStephan Agricola: Stephan Agricola (c. 1491–1547) was a Lutheran church reformer.  Born in Abensberg, at a young age he joined the Augustinian order.  As a monk, he studied Augustine deeply.  As a student, he went to the universities in Bologna and Venice, where in 1519 he became a Doctor of Theology.  He began to preach on whole books of the Bible in 1520.  He was led to Lutheranism through his study of Augustine's works on the scriptures.  He was accused of Lutheranism as a heresy.  Although he claimed his independence of Luther, he was arrested and imprisoned in Mühldorf on November 17, 1522.  In 1523 he escaped and came to Augsburg, where with Urbanus Rhegius he fully accepted the Reformation and translated Johannes Bugenhagen's tract \"ag.  Zwingjli\" into German.  He was on the Lutheran side during the Marburg Colloquy, became pastor in Hof in 1532, took part in the meeting at Schmalkalden in 1537, and signed the Smalcald Articles.  He was instrumental in introducing the Reformation in the Upper Palatinate, as he was pastor at Sulzbach beginning in 1542.  During the Schmalkaldic War, he had to flee to Eisleben, where he died in old age on April 10–11, 1547.  Stephen Agricola was a staunch uncompromising Lutheran, earnest and devoted.  His son, Stephen, translated some of Luther's commentaries on the minor prophets.\n\nAnne Locke: Anne Locke (Lock, Lok) (1530 – after 1590) was an English poet, translator and Calvinist religious figure.  She was the first English author to publish a sonnet sequence, \"A Meditation of a Penitent Sinner\" (1560).\n\nHoly Sonnets: The Holy Sonnets—also known as the Divine Meditations or Divine Sonnets—are a series of nineteen poems by the English poet John Donne (1572–1631).  The sonnets were first published in 1633—two years after Donne's death.  The poems are sonnets and are predominantly in the style and form prescribed by Renaissance Italian poet Petrarch (or Francesco Petrarca) (1304–1374) in which the sonnet consisted of two quatrains (four-line stanzas) and a sestet (a six-line stanza).  However, several rhythmic and structural patterns as well as the inclusion of couplets are elements influenced by the sonnet form developed by English poet and playwright William Shakespeare (1564–1616).\n\nRobert Browning: Robert Browning (7 May 1812 – 12 December 1889) was an English poet and playwright whose mastery of the dramatic monologue made him one of the foremost Victorian poets.  His poems are known for their irony, characterization, dark humour, social commentary, historical settings, and challenging vocabulary and syntax.\n\nJohannes Agricola in Meditation: \"Johannes Agricola in Meditation\" (1836) is an early dramatic monologue by Robert Browning.  The poem was first published in the \"Monthly Repository\"; later, it appeared in \"Dramatic Lyrics\" (1842) paired with \"Porphyria's Lover\" under the title \"Madhouse Cells.\"\n\nPorphyria's Lover: \"Porphyria's Lover\" is a poem by Robert Browning which was first published as \"Porphyria\" in the January 1836 issue of \"Monthly Repository\".  Browning later republished it in \"Dramatic Lyrics\" (1842) paired with \"Johannes Agricola in Meditation\" under the title \"Madhouse Cells\".  The poem did not receive its definitive title until 1863.\n\nThomas Hood: Thomas Hood (23 May 1799 – 3 May 1845) was an English poet, author and humorist, best known for poems such as \"The Bridge of Sighs\" and \"The Song of the Shirt\".  Hood wrote regularly for \"The London Magazine\", the \"Athenaeum\", and \"Punch\".  He later published a magazine largely consisting of his own works.  Hood, never robust, lapsed into invalidism by the age of 41 and died at the age of 45.  William Michael Rossetti in 1903 called him \"the finest English poet\" between the generations of Shelley and Tennyson.  Hood was the father of playwright and humourist Tom Hood (1835–1874).\n\nQuestion: When was the  English poet who created Johannes Agricola in Meditation born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"poet\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the poet.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the poet.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the poet in 'Day Month Year' format.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"birth_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"poem_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the poem in question.\"\n    },\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The specific question asked about the poet's birth date.\"\n    }\n  },\n  \"required\": [\n    \"poet\",\n    \"poem_title\",\n    \"question_asked\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "poet": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the poet."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the poet."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the poet in 'Day Month Year' format."
          }
        },
        "required": [
          "name",
          "nationality",
          "birth_date"
        ],
        "additionalProperties": false
      },
      "poem_title": {
        "type": "string",
        "description": "The title of the poem in question."
      },
      "question_asked": {
        "type": "string",
        "description": "The specific question asked about the poet's birth date."
      }
    },
    "required": [
      "poet",
      "poem_title",
      "question_asked"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

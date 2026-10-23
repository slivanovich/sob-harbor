{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Sun Rising (poem): The Sun Rising (also known as \"The Sunne Rising\") is a thirty line poem with three stanzas published in 1633 by poet John Donne.  The meter is irregular, ranging from two to six stresses per line in no fixed pattern.  The longest lines are at the end of the three stanzas and the rhyme never varies—each stanza runs 'abbacdcdee'.  Donne's poems were known to be metaphysical with jagged rhythms, dramatic monologues, playful intelligence, and startling images.  The poem personifies the sun and stanza one begins with the speaker in bed with his lover, complaining about its beaming rays.  Donne uses expressions such as, \"Busy old fool\" (line 1) and \"Saucy Pedantic Wretch\" [perfectionist] (line 5) to describe his annoyance with it.  The speaker of the poem questions the sun's motives and yearns for the sun to go away so that he and his lover can stay in bed.\n\nGertrude and Claudius: Gertrude and Claudius is a novel by John Updike.  It uses the known sources of Shakespeare's \"Hamlet\" to tell a story that draws on a rather straightforward revenge tale in the medieval Denmark depicted by Saxo Grammaticus in his twelfth-century \"Historiae Danicae\", but incorporates extra plot elements added by François de Belleforest in his \"Histoires tragiques\", published in 1576.  And, finally, it brings in various elements from Shakespeare's play, including the name \"Corambis\" for Polonius from the \"bad quarto\" of 1603.  This story, in its three forms, is primarily concerned with Hamlet (or \"Amleth\" in Saxo) avenging his father's murder, but the story starts earlier.  The novel is concerned with that earlier life of Gertrude, Claudius, and old Hamlet, and it ends at the close of Act I, scene ii of \"Hamlet\".\n\nOphelia: Ophelia is a character in William Shakespeare's play \"Hamlet\".  She is a young noblewoman of Denmark, the daughter of Polonius, sister of Laertes, and potential wife of Prince Hamlet.  She is one of only two female characters in the play.\n\nLe jeune sage et le vieux fou: Le jeune sage et le vieux fou (\"The Wise Young Man and the Old Fool\") is an opera by the French composer Étienne Méhul with a libretto by François-Benoît Hoffman.  It takes the form of a \"comédie mêlée de musique\" (a type of \"opéra comique\") in one act.  It was first performed at the Théâtre Favart on 28 March 1793.  A revised version appeared in 1801.\n\nGhost (Hamlet): The ghost of Hamlet's late father is a character from William Shakespeare's play \"Hamlet\".  In the stage directions he is referred to as \"Ghost.\"  His name is also Hamlet, and he is referred to as \"King\" Hamlet to distinguish him from the Prince.\n\nBaron Bodissey: Unspiek, Baron Bodissey, is a fictional character referred to in many of the novels of speculative-fiction author Jack Vance.  Within those novels he has the status of an authority, but he is sometimes referred to with amusement or scepticism.  Like the 'mad poet' Navarth, he first appeared in the Demon Princes sequence but also is alluded to in a number of other unrelated stories.  Unlike Navarth, the Baron never appears in person in these novels, but his monumental, many-volume work \"Life\" is frequently quoted.  The lengthiest citations from it appear, with varying degrees of apparent relevance, as epigraphs to various chapters in the \"Demon Princes\" novels.  (Vance characteristically makes use of substantial passages from imaginary writings, interviews or judicial transcripts as chapter-heading material, especially in that series.)  Otherwise, the Baron and his work are occasionally referred to in passing or quoted by characters in the tales.  Fictional (and always negative) reviews of \"Life\" also appear in The Killing Machine and The Face, usually dismissing it as snobbish, elitist and pretentious; one reviewer expresses a desire to thrash the Baron within an inch of his life before buying him a drink.\n\nPolonius: Polonius is a character in William Shakespeare's \"Hamlet\".  He is chief counsellor of the king, and the father of Laertes and Ophelia.  Generally regarded as wrong in every judgment he makes over the course of the play, Polonius is described by William Hazlitt as a \"sincere\" father, but also \"a busy-body, [who] is accordingly officious, garrulous, and impertinent\".  In Act II Hamlet refers to Polonius as a \"tedious old fool\" and taunts him as a latter day \"Jeptha\".\n\nBanalata Sen: Banalata Sen (Bengali: বনলতা সেন ) is a Bengali poem written in 1942 by the poet Jibanananda Das that is one of the most read, recited and discussed poems of Bengali literature.  The title of this lyric poem is a female character referred to by name in the last line of each of its three stanzas.  A draft of the poem was also discovered that widely differs from the final version.  Poet Jibanananda Das was a quiet person, who preferred to live in obscurity.  Until the discovery of his diaries in the mid-1990s, it was considered unlikely that he could have been in love with a woman with or without the name of Banalata Sen. However, Banalata Sen of Natore, a tiny town in the Rajshahi area of what was then Bengal, has become an emblem of feminine mystery as well as beauty and love.\n\nUnseen character: An unseen character or (in radio) silent character is a fictional character referred to but not directly observed by the audience, but who advances the action of the plot in a significant way, and whose absence enhances their effect on the plot.\n\nHamlet (Liszt): Hamlet, S.104, is a symphonic poem by Franz Liszt, written in 1858 and published as No. 10.  It was not performed until 2 July 1876.  Like all but one of Liszt's 13 symphonic poems, \"Hamlet\" was written while Liszt was working in Weimar and is dedicated to Carolyne zu Sayn-Wittgenstein.  After viewing Bogumil Dawison play Hamlet in Weimar (1856), Liszt wrote: \"He does not make him into an indecisive dreamer who collapses under the power of his mission, as he is regarded since Goethe's theory in \"Wilhelm Meister\", but much more as a gifted, enterprising prince with important political views who is waiting for the right moment to complete his work of revenge and come to the aim of his ambition, that is, to be crowned king in place of his uncle.  This goal can naturally not be reached in twenty-four hours and the clever anticipation which Shakespeare has put into the role of Hamlet and the negotiations with England which come clearly to the light of day at the end of the drama according to my view justify Dawson's interpretation, which Herr von Goethe and the aesthetes should not take too badly.  Regarding Ophelia, Liszt wrote: \"She is loved by Hamlet, but Hamlet, like every exceptional person, imperiously demands the wine of life and will not content himself with the buttermilk.  He wishes to be understood by her without the obligation of explaining himself to her.  She collapses under her mission, because she is incapable of loving him in the way that he must be loved, and her madness is only the decrescendo of her feeling, whose lack of sureness has not allowed her to remain on the level of Hamlet.\"  Liszt's \"Hamlet\" is meant as a psychological study of the title character; only two brief references are made to Ophelia, both marked as \"to be played as quietly as possible and sound like a shadowy picture.\"\n\nQuestion: In Shakespeare's Hamlet, what is the name of the daughter of the character referred to as a tedious old fool by Hamlet?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"play_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the play.\"\n        },\n        \"author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the play.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"author\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"referred_character\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character referred to by Hamlet.\"\n        },\n        \"description_by_hamlet\": {\n          \"type\": \"string\",\n          \"description\": \"The specific phrase Hamlet uses to describe this character.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the referred character in the play.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"description_by_hamlet\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"daughter_character\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the daughter of the referred character.\"\n        },\n        \"relationship_to_referred_character\": {\n          \"type\": \"string\",\n          \"description\": \"The relationship of this character to the referred character.\"\n        },\n        \"other_relationships\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Other significant relationships of the daughter character.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"relationship_to_referred_character\",\n        \"other_relationships\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"play_details\",\n    \"referred_character\",\n    \"daughter_character\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "play_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the play."
          },
          "author": {
            "type": "string",
            "description": "The author of the play."
          }
        },
        "required": [
          "title",
          "author"
        ],
        "additionalProperties": false
      },
      "referred_character": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the character referred to by Hamlet."
          },
          "description_by_hamlet": {
            "type": "string",
            "description": "The specific phrase Hamlet uses to describe this character."
          },
          "role": {
            "type": "string",
            "description": "The role of the referred character in the play."
          }
        },
        "required": [
          "name",
          "description_by_hamlet",
          "role"
        ],
        "additionalProperties": false
      },
      "daughter_character": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the daughter of the referred character."
          },
          "relationship_to_referred_character": {
            "type": "string",
            "description": "The relationship of this character to the referred character."
          },
          "other_relationships": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other significant relationships of the daughter character."
          }
        },
        "required": [
          "name",
          "relationship_to_referred_character",
          "other_relationships"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "play_details",
      "referred_character",
      "daughter_character"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

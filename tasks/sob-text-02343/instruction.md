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
Freedom in Exile: Freedom in Exile: The Autobiography of the Dalai Lama is the second autobiography of the 14th Dalai Lama, released in 1991.  The Dalai Lama's first autobiography, "My Land and My People", was published in 1962, a few years after he reestablished himself in India and before he became an international celebrity.  He regards both of the autobiographies as authentic and re-issued "My Land and My People" in 1997 to coincide with the release of the film "Kundun".

Khashyar Darvich: Khashyar Darvich is a documentary film producer and director best known for directing a documentary film about the Dalai Lama, "Dalai Lama Renaissance," which is narrated by actor Harrison Ford.

Thubten Chodron: Thubten Chodron, born Cheryl Greene, is an American Tibetan Buddhist nun, author, teacher, and the founder and abbess of Sravasti Abbey, the only Tibetan Buddhist training monastery for Western nuns and monks in the United States.  Chodron is a central figure in the reinstatement of the Bhikshuni (tib.  Gelongma) ordination of women.  She is a student of the 14th Dalai Lama, Tsenzhab Serkong Rinpoche, Lama Thubten Yeshe, Thubten Zopa Rinpoche, and other Tibetan masters.  She has published many books on Buddhist philosophy and meditation, and is the only nun who has co-authored a book with the Dalai Lama—"Buddhism: One Teacher, Many Traditions".

Barry Kerzin: Barry Michael Kerzin, M.D., (born November 1, 1947) is an American physician and Buddhist monk.  He has lived in Dharamshala since 1988 and serves as a personal physician to the 14th Dalai Lama, along with treating people in the local community, free of charge.  Following his ordination as a monk by the Dalai Lama in the mid-2000s, he has travelled widely, teaching and offering workshops in which he blends Buddhist teaching and his medical training, emphasizing the spiritual and health benefits of meditation and compassion.  He has served as a research subject in neuroscience research into the effects of meditation on the brain.

Dalai Lama Renaissance: Dalai Lama Renaissance is a 2007 feature-length documentary film, produced and directed by Khashyar Darvich, and narrated by actor Harrison Ford.  The film documents the Dalai Lama's meeting with the self-titled "Synthesis" group, made up of 40 Western "renaissance" thinkers who hope to use the meeting to change the world and resolve many of the world's problems.  The meeting took place at the Dalai Lama's home in Dharamsala, India in September, 1999.

Jeffrey Hopkins: Jeffrey Hopkins (born 1940) is an American Tibetologist.  He is Emeritus of Tibetan and Buddhist Studies at the University of Virginia, where he taught for more than three decades since 1973.  He has authored more than twenty-five books about Tibetan Buddhism, among them the highly influential "Meditation on Emptiness", which appeared in 1983, offering a pioneering exposition of Prasangika-Madyamika thought in the Geluk tradition.  From 1979 to 1989 he was the Dalai Lama's chief interpreter into English and he played a significant role in the development of the Free Tibet Movement.  In 2006 he published his English translation of a major work by the Jonangpa lama, Dolpopa, on the Buddha Nature and Emptiness called "Mountain Doctrine".

Tibetan Parliament in Exile election, 1960: The first election for the then named Tibetan Assembly was held on September 2, 1960, as part of a process of democratization of the Tibetan community encourage by the Dalai Lama.  The election for Parliament was announced by the Dalai Lama in a trip to Bodh Gaya on January of the same year.  This was the first time in history that Tibetans could elect their political leaders and September 2 is currently celebrate among the Tibetan diaspora as “Democracy Day”.  One of the first decisions of the Assembly was to abolish all hereditary titles and functions of the old aristocracy, Buddhist hierarchy and tribal leaders declaring the equality of all Tibetans.  Since that, other 15 assemblies have been elected.

Tibetan Institute of Performing Arts: The Tibetan Institute of Performing Arts (TIPA) was founded by Tenzin Gyatso, the 14th Dalai Lama on reaching McLeod Ganj, Himachal Pradesh, India in exile from Tibet in August 1959.  It was then called Tibetan Music, Dance and Drama Society, which was one of the first institutes set up by the Dalai Lama, and was established to preserve Tibetan artistic heritage, especially opera, dance, and music.

American Bellydancer: American Bellydancer is a 2005 documentary film directed by Jonathan Brandeis.  It features Bellydancers including Ansuya, Rachel Galoob-Ortega, Suhaila Salimpour, Rachel Brice and Sonia.

9th Dalai Lama: The 9th Dalai Lama (religious name: Lungtok Gyatso, shortened from Lobzang Tenpai Wangchuk Lungtok Gyatso; 1 December 18056 March 1815), also spelled Lungtog Gyatso and Luntok Gyatso, was the 9th Dalai Lama of Tibet.  He was the only Dalai Lama to die in childhood and was first of a string of four Dalai Lamas to die before reaching 22 years of age.

Question: Was American Bellydancer or Dalai Lama Renaissance released first?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "string",
      "description": "Indicates which film was released first."
    },
    "films": {
      "type": "array",
      "description": "Details of the films being compared.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the film was released."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      }
    },
    "first_released_film_title": {
      "type": "string",
      "description": "The title of the film that was released first."
    },
    "first_released_year": {
      "type": "integer",
      "description": "The year the first film was released."
    }
  },
  "required": [
    "comparison_result",
    "films",
    "first_released_film_title",
    "first_released_year"
  ],
  "additionalProperties": false
}

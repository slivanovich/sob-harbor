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
Hillel Street: Hillel Street (Hebrew: רחוב הלל‎ ‎ , "Rehov Hillel") is one of the central streets of Jerusalem.  It connects King George Street to the small Ben Sira Street and the Mamilla neighbourhood and is parallel to Ben Yehuda Street.  The lower part of the road is between Independence Park and the Nahalat Shiva neighborhood.

David Penchansky: David Penchansky is a professor in the field of Hebrew Bible.  In his writing, he applies the methodology of literary criticism to the Old Testament, particularly its Wisdom Literature (the books of Job, Proverbs, Ecclesiastes, Ben Sira and the Wisdom of Solomon).  Both Marxism and Deconstruction have influenced his approach.

Sirach: The Book of the All-Virtuous Wisdom of Joshua ben Sira, commonly called the Wisdom of Sirach or simply Sirach, and also known as the Book of Ecclesiasticus (abbreviated Ecclus.)  or Ben Sira, is a work of ethical teachings, from approximately 200 to 175 BCE, written by the Jewish scribe Ben Sira of Jerusalem, on the inspiration of his father Joshua son of Sirach, sometimes called Jesus son of Sirach or Yeshua ben Eliezer ben Sira.

Alphabet of Sirach: The Alphabet of ben Sirach ("Alphabetum Siracidis", "Othijoth ben Sira") is an anonymous medieval text inspired by the Wisdom of Sirach.  It is dated to anywhere between 700 and 1000 CE.  It is a compilation of two lists of proverbs, 22 in Aramaic and 22 in Hebrew, both arranged as alphabetic acrostics. Each proverb is followed by an Haggadic commentary.  The work has been characterized as satirical, and it contains references to masturbation, incest and flatulence.  The text has been translated into Latin, Yiddish, Judeo-Spanish, French and German.  A partial English translation appeared in Stern and Mirsky (1998).

The Clear Word: The Clear Word, originally published in March 1994 as the "Clear Word Bible", is an English-language "devotional paraphrase of the Bible expanded for clarity".  It is an interpretive text of the Bible written as a personal devotional exercise by Jack Blanco, former dean of the School of Religion at Southern Adventist University, to be an additional study tool and devotional alongside the Bible.  Major portions of the translation are material added by the author.  It is printed in chapter-and-verse format, two columns to a page.

1 Maccabees: 1 Maccabees is a book of the Bible written in Hebrew by a Jewish author after the restoration of an independent Jewish kingdom by the Hasmonean dynasty, about the latter part of the 2nd century BC.  The original Hebrew is lost and the most important surviving version is the Greek translation contained in the Septuagint.  The book is held as canonical scripture by the Catholic, Orthodox, and Oriental Orthodox churches (except for the Orthodox Tewahedo), but not by Anglican and Protestant denominations.  Such Protestants consider it to be an apocryphal book (see also Deuterocanon).  In modern-day Judaism, the book is often of great historical interest, but has no official religious status.

Ben Sira: Ben Sira, also known as Shimon ben Yeshua ben Eliezer ben Sira or Jesus Ben Sira, (fl.  2nd century BCE) was a Hellenistic Jewish scribe, sage, and allegorist from Jerusalem.  He is the author of the Book of Sirach, also known as the Book of Ecclesiasticus.

The Jesus Storybook Bible: The Jesus Storybook Bible is a children's Bible written by "New York Times" bestselling author Sally Lloyd-Jones and illustrated by Jago from Cornwall.  The first edition was published in 2007 by Zonderkidz, the children's arm of American Christian media and publishing company Zondervan.

Isaiah scroll: The Isaiah Scroll, designated 1Qlsa and also known as the Great Isaiah Scroll, is one of the seven Dead Sea Scrolls that were first recovered by Bedouin shepherds in 1947.  The scroll is written in Hebrew and contains the entire Book of Isaiah from beginning to end, apart from a few small damaged portions.  It is the oldest complete copy of the Book of Isaiah known, being 1100 years older than the Leningrad Codex, and the most complete scroll out of the 220 found at Qumran.  Pieces of the Isaiah Scroll have been carbon-14 dated at least four times, giving calibrated date ranges between 356-103 BC; there have also been numerous paleographic and scribal dating studies placing the scroll around 150-100 BC.

Roy Kinneer Patteson, Jr.: Dr. Roy Kinneer Patteson, Jr. was an American scholar whose knowledge of Biblical Hebrew, Aramaic, Syriac and Hellenistic Greek enabled him to undertake an analysis of the text of the Ben Sira Scroll discovered at Masada in Palestine in 1964.  His research resulted in the establishment of a critical Hebrew text for portions of the first-century B.C. book, Sirach.

Question: The scholar who analyzed the Ben Sira scroll added portions to a book of the Bible  written by the author on the inspiration of who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "scholar_name": {
      "type": "string",
      "description": "The name of the scholar who analyzed the scroll."
    },
    "scroll_analyzed": {
      "type": "string",
      "description": "The name of the scroll analyzed by the scholar."
    },
    "book_name": {
      "type": "string",
      "description": "The name of the book that the scholar's research established a critical text for."
    },
    "book_author": {
      "type": "string",
      "description": "The author of the book."
    },
    "author_inspiration_source": {
      "type": "string",
      "description": "The person who inspired the author of the book."
    }
  },
  "required": [
    "scholar_name",
    "scroll_analyzed",
    "book_name",
    "book_author",
    "author_inspiration_source"
  ],
  "additionalProperties": false
}

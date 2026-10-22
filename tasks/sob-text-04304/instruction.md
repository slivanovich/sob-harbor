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
Second Temple period: The Second Temple period in Jewish history lasted between 530 BCE and 70 CE, when the Second Temple of Jerusalem existed.  The sects of Pharisees, Sadducees, Essenes, and Zealots were formed during this period.  The Second Temple period ended with the First Jewish–Roman War and the Roman destruction of Jerusalem and the Temple.

Bnei Bathyra: Bnei Bathyra (Hebrew: בני בתירא‎ ‎ , lit. " "The Children of Bathyra""; Also referred to in the Jerusalem Talmud as זקני בתירא, lit. " "The Elders of Bathyra"") were Jewish sages family that in a certain period of time, headed the religious leadership of the Jewish people, during the Destruction of the Second Temple, and in close proximity to the beginning of the era of the Tannaim.  This family is known for its many important Jewish Sages over the course of many generations.  A hundred-year before the Destruction of the Second Temple, the family's sages have passed the torch of the Jewish leadership to Hillel the Elder, that made Aliya to the Land of Israel from Babylon and had studied at Sh'maya and Abtalion.  The sages of the family are considered "Gedolei Hador", the intellectual giants of the religious world of these generations, even after the Destruction of the Second Temple, and are known to have held a prominent position among the Yavne Sages.  The general consensus attributes some Tannaim to this family, and the most known of these attributions is Judah ben Bathyra, who resided in Nusaybin west to Babylon.

Dafo Temple (Guangzhou): The Dafo Temple (; literally Grand Buddha Temple) is a Buddhist temple in Guangzhou, Guangdong, China.  Located in Yuexiu District, Dafo Temple is a grand temple with a history of more than one thousand years and was built by Emperor Liu Yan in the Southern Han dynasty (917–971).  It has been praised as one of the "Five Largest Temples of Guangzhou" in history.  Later it was destroyed and rebuilt for many times.  In the late Ming dynasty, the temple was declining day by day and was devastated by the war while Shang Kexi and Geng Jimao conquered Guangdong in 1649.  During the reign of Emperor Kangxi in 1663, the temple was rebuilt and expanded by Shang Kexi continuously.  According to the national policy of free religious belief, the temple was approved by Guangzhou Municipal People's Government to be recovered into Buddhist temple in 1981.  Then Master Guangming, vice-president of the Guangzhou Buddhist Association, served as abbot, he tried to revitalize Dafo Temple and made it re-show the style of the large temple.  On August 9, 1993, Dafo Temple was put on the list as a Municipality Protected Historic Site by the Guangzhou Municipal People's Government.

Third Temple: The Third Temple (Hebrew: בית המקדש השלישי‎ ‎ : "Beit haMikdash haShlishi" lit.  (The) House, the Holy, the Third) refers to a number of viewpoints, expectations and projects regarding the building of a third temple in Jerusalem.  This Temple would be the third central religious space for Jews after Solomon's Temple and the rebuilt Second Temple.  Although it has not been built, prospects for its completion are important in Jewish eschatology.

Solomon's Temple: According to the Hebrew Bible, Solomon's Temple, also known as the First Temple, was the Holy Temple (Hebrew: בֵּית־הַמִּקְדָּשׁ‎ ‎ : "Beit HaMikdash") in ancient Jerusalem before its destruction by Nebuchadnezzar II after the Siege of Jerusalem of 587 BCE and its subsequent replacement with the Second Temple in the 6th century BCE.

New Jerusalem: In the Book of Ezekiel in the Hebrew Bible, New Jerusalem (, "Jehovah-shammah", or "[where] YHWH [is] there") is Ezekiel's prophetic vision of a city centered on the rebuilt Holy Temple, the Third Temple, to be established in Jerusalem, which would be the capital of the Messianic Kingdom, the meeting place of the twelve tribes of Israel, during the Messianic era.  The prophecy is recorded by Ezekiel as having been received on Yom Kippur of the year 3372 of the Hebrew calendar.  It will be inhabited by people to live eternally in spirit form, created by God as a gift to mankind.  Not everyone will reside in New Jerusalem, as most will possibly stay on Earth.

Andrei Orlov (historian): Andrei A. Orlov is an American professor of Judaism and Christianity in Antiquity at Marquette University.  He "is a specialist in Jewish Apocalypticism and Mysticism, Second Temple Judaism, and Old Testament Pseudepigrapha.  Within the field of Second Temple Jewish apocalyptic literature, Orlov is considered among the leading experts in the field of Slavonic texts related to Jewish mysticism and Enochic traditions."  He "has established himself as a significant voice in the study of Second Temple Jewish traditions, especially those associated with 2 Enoch and other Slavonic Pseudepigrapha."  Orlov is a veteran of the Enoch seminar and a member of the Advisory Board of the journal "Henoch".

Jerusalem during the Second Temple Period: Jerusalem during the Second Temple period describes the history of the city from the return to Zion under Cyrus the Great to the 70 CE siege of Jerusalem by Titus during the First Jewish–Roman War, which saw both region and city change hands several times.  It was the center of religious life for all Jews, even those who lived in the diaspora prayed towards Jerusalem on a daily basis and made pilgrimages during religious festivals.  The Pharisees of Second Temple Judaism developed into the Tannaim and Judaism's post-Exilic religious identity as it continues today, and the Hebrew Bible was perhaps canonized, although exactly when this occurred remains disputed.  It was also in Jerusalem during the later stages of this period that Christianity was born.

Second Temple Judaism: Second Temple Judaism is Judaism between the construction of the Second Temple in Jerusalem, c. 515 BCE, and its destruction by the Romans in 70 CE.  The development of the Hebrew Bible canon, the synagogue, Jewish apocalyptic expectations for the future, and Christianity, can all be traced to the Second Temple period.

Second Temple: The Second Temple (Hebrew: בֵּית־הַמִּקְדָּשׁ הַשֵּׁנִי‎ ‎ , "Beit HaMikdash HaSheni") was the Jewish Holy Temple which stood on the Temple Mount in Jerusalem during the Second Temple period, between 516 BCE and 70 CE.  According to Jewish tradition, it replaced Solomon's Temple (the First Temple), which was destroyed by the Babylonians in 586 BCE, when Jerusalem was conquered and part of the population of the Kingdom of Judah was taken into exile to Babylon.

Question: What book of the Bible talks about the third central religious space for Jews after Solomon's Temple and the rebuilt Second Temple?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "temple_name": {
      "type": "string",
      "description": "The name of the temple being referred to."
    },
    "temple_description": {
      "type": "string",
      "description": "A description of the temple's significance or order."
    },
    "preceding_temples": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of temples that preceded the one in question."
    },
    "biblical_book_of_mention": {
      "type": "string",
      "description": "The book of the Bible where the temple is mentioned."
    },
    "mention_context": {
      "type": "string",
      "description": "The context in which the temple is mentioned in the biblical book."
    },
    "associated_vision_name": {
      "type": "string",
      "description": "The name of the prophetic vision associated with the temple."
    }
  },
  "required": [
    "temple_name",
    "temple_description",
    "preceding_temples",
    "biblical_book_of_mention",
    "mention_context",
    "associated_vision_name"
  ],
  "additionalProperties": false
}

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
Hero Heel: Hero Heel (HERO・HEEL -英雄と悪漢- , Hero Heel - Eiyū to Akkan ) is a Japanese manga written and illustrated by Makoto Tateno.  It is licensed in North America by Digital Manga Publishing, which released the manga through its imprint, Juné, on April 8, 2008.  Biblos released the manga on August 10, 2005 before it went bankrupt in 2006.  Libre Publishing took over publication in Japan and released the manga's three "tankōbon" between June 30, 2007 and March 10, 2007, publishing the last two volumes first then the first volume.  The manga is licensed in Taiwan by Egmont Manga & Anime and in Germany by AnimePro.

Aqua Bless: Aqua Bless (アクアブレス , Akua Buresu ) is an erotic one-shot Japanese manga written and illustrated by Yamatogawa.  The manga was serialized in Akane Shinsha's manga magazine "Comic Tenma".  Akaneshinsha released the manga in Japan in February 2007.  The manga is licensed and licensed in North America by Icarus Publishing, which released the manga on November 4, 2008.  Digital Manga, under its Project-H imprint, has licensed the manga in North America for both digital and print release in 2014.

Seito Shokun!: Seito Shokun!  (Japanese: 生徒諸君!  , lit.  "Attention Students!")  is a Japanese manga written and illustrated by Yōko Shōji.  It is serialized in Kodansha's "Shōjo Friend" from 1977 to 1984.  The individual chapters were published into 24 "tankōbon" by Kodansha between February 1978 and June 1985.  "Seito Shokun!"  won the second Kodansha Manga Award in 1978 for the shōjo category.

Yōko Shōji: Yōko Shōji (庄司 陽子 , Shōji Yōko , born 4 June 1950, in Mobara, Chiba) is a Japanese manga artist.  She is best known for writing "Seito Shokun! " ("Attention Students!") , for which she won the Kodansha Manga Award for shōjo in 1978.

Ruff Love: Ruff Love (Japanese: シバといっしょ。 , Hepburn: Shibato Issho. )  is a one-shot Japanese manga written and illustrated by Tamaki Kirishima.  The manga was serialized in Nihonbungeisha's manga magazine, "Nichibun Comics".  Nihonbungeisha released the manga's "tankōbon" volume on December 28, 2006.  It is licensed in North America by Aurora Publishing, which released the manga through its yaoi imprint, Deux Press, on August 8, 2008.  The manga is licensed in Taiwan by Ever Glory Publishing, which released the manga on October 5, 2007.

Dragon Eye (manga): Dragon Eye (Japanese: 龍眼－ドラゴンアイ－ , Hepburn: Ryū Gan -Doragon Ai- ) is a Japanese manga written and illustrated by Kairi Fujiyama.  The manga was serialized in Kodansha's manga magazine, "Monthly Shōnen Sirius".  The manga is licensed in North America by Del Rey Manga.  Since early 2008, the series has been on hiatus in Japan, apparently due to the creator's illness.  The manga features a squadron of fighters (called VIUS)who are immune to "D-virus" and the Dracule which is a group of creatures who spread the "D-virus".

Sexy Commando Gaiden: Sugoi yo!! Masaru-san: Sexy Commando Gaiden: Sugoi yo!!  Masaru-san (Japanese: セクシーコマンドー外伝 すごいよ!! マサルさん , Hepburn: Sekushī Komandō Gaiden: Sugoi yo!!  Masaru-san , lit.  Sexy Commando Side Story: That's Amazing!!  Mr. Masaru) is a Japanese manga written and illustrated by Kyosuke Usuta.  The manga (79 chapters in total) appeared in "Weekly Shōnen Jump" from 1995 to 1997.  In 1998, it was turned into an animation by the Japanese network TBS and ran 48 seven-minute episodes as part of the television show block "Wonderful".  The anime follows the first 48 chapters of the manga nearly word for word, for the dialogue used in the series and the scenes drawn were lifted directly from the manga panels.

The Four Immigrants Manga: The Four Immigrants Manga, also known as Manga of the Four Students (漫画四人書生 , Manga Yonin Shosei ) , is a Japanese manga written and illustrated by Henry Yoshitaka Kiyama.  The manga was published as 52 "episodes", with each episode as a two-page-spread with the intention of serialization in a Japanese language newspaper.  The individual episodes were self published by Kiyama as a one-shot manga in 1931.  It was republished in Japan by Shimpu in August 2012.  It was translated into English by Frederik L. Schodt and was published by Stone Bridge Press as "The Four Immigrants Manga: A Japanese Experience in San Francisco 1904–1924" in October 1998.

My Generation/Understand: "My Generation/Understand" is the ninth single by the Japanese artist Yui.  Even though this is a double-A single, "Understand" is not included on the album "I Loved Yesterday", but the song is included in the B-side compilation album, "My Short Stories".  "My Generation" was used as the theme song for the drama Seito Shokun! .

Shōji Satō (artist): Shōji Satō (佐藤 ショウジ , Satō Shōji ) is a Japanese manga artist who does hentai and non-hentai artwork.  He has also published various "dōjinshi" under the pen name Inazuma and runs a hentai genre manga artist group called Digital Accel Works.  He is responsible for the character design and illustration for the "Highschool of the Dead" manga.  He is the former assistant of manga artist Kōshi Rikudō, the creator of the popular manga series "Excel Saga".

Question:  My Generation/Understand was used as the theme song for what Japanese manga written and illustrated by Yōko Shōji

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "manga_title": {
      "type": "string",
      "description": "The title of the Japanese manga."
    },
    "author_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the manga artist."
        },
        "role": {
          "type": "string",
          "description": "The role of the artist (e.g., writer and illustrator)."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "theme_song_details": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the theme song."
        },
        "artist": {
          "type": "string",
          "description": "The artist of the theme song."
        }
      },
      "required": [
        "song_title",
        "artist"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "manga_title",
    "author_details",
    "theme_song_details"
  ],
  "additionalProperties": false
}

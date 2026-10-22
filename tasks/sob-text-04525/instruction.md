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
Howard Staunton: Howard Staunton (1810 – 22 June 1874) was an English chess master who is generally regarded as having been the world's strongest player from 1843 to 1851, largely as a result of his 1843 victory over Saint-Amant.  He promoted a chess set of clearly distinguishable pieces of standardised shape—the Staunton pattern promulgated by Nathaniel Cook—that is still the style required for competitions.  He was the principal organiser of the first international chess tournament in 1851, which made England the world's leading chess centre and caused Adolf Anderssen to be recognised as the world's strongest player.

Staunton chess set: The Staunton chess set is composed of a particular style of chess pieces used to play the game of chess.  According to the rules of chess, this style is to be used for competitions.  Nathaniel Cook is credited with the design, and they are named after Howard Staunton.  The first 500 sets were hand signed and numbered by Staunton.  This style of set was first made available by Jaques of London in 1849, and they quickly became the standard.  They have been used around the world since.

Selenus chess set: The Selenus chess set is one of the most elegant classical chess set styles in use before the standardization of chess pieces that happened after the Staunton chess set was launched, in 1849 by John Jaques of London games manufacturer.  The Selenus sets, were typical of Germany and Northern Europe and named after Gustavus Selenus, the pen name of Augustus the Younger, Duke of Brunswick-Lüneburg, author of the Chess or the King's Game (German: Das Schach- oder Königsspiel), an important chess manual published in the 17th century.  The standard included delicate lathe turned bases and shafts and tiers with circlets resembling crowns.  Pieces were distinguished by heights, the number of tiers and sometimes by symbols.

Pinnacle Brands: Pinnacle Brands was a trading card company from 1988 to 1998.  With its first baseball card set called Score, it changed the baseball card industry from the "Big Three" (Donruss, Fleer, Topps) that had been in place for seven years prior.  Score's first set used a bold colorful border design (with 110 cards each in red, orange, yellow, green, blue, and violet borders) and was the first major set to have a color mugshot of the player and was the first major set besides 1982 Fleer to have a full color back.  The player biographies were by far the most extensive of any major baseball card set of its time.  The 1991 and 1992 sets at 900 (1991) 910 (1992) cards were among the largest card sets of that time.

9th Chess Olympiad: The 9th Chess Olympiad, organized by the FIDE and comprising an open team tournament, as well as several events designed to promote the game of chess, took place between August 20 and September 11, 1950, in Dubrovnik, PR Croatia, FPR Yugoslavia (present day Croatia).  84 players from 16 nations played a total of 480 games.  The acclaimed 1950 Dubrovnik chess set was designed and manufactured specifically for the Olympiad.

Dubrovnik chess set: The Dubrovnik chess set has chess pieces of a particular type influenced by the Staunton chess set and used to play the game of chess.  These chessmen are considered to have significant historical importance and are a timeless design classic.  Over the decades the Dubrovnik chessmen were redesigned several times.

Gökyay Association Chess Museum: The Gökyay Association Chess Museum is located in Altındağ, Ankara, Turkey and displayed in a historical home.  The museum has the largest chess set collection in the world with 570 chess sets collected from 103 countries exhibited under four main themes in a 1,008 square metre area.  There are a variety chess sets representing various cultures and made with materials including wood, metal, fishbone, marble, soapstone, felt, polyester, metal, marble, sheet metal and cast iron.

Chess set: A chess set has thirty-two chess pieces in two colours and a chessboard used to play chess.  Chess is played by two chess players with each player starting with one king, one queen, two rooks, two bishops, two knights and eight pawns. Chess equipment often accompanying a chess set are a chess box, chess clock and chess table.  Chess sets are made in a wide variety of styles, often for ornamental rather than practical purposes.  For tournament play, the Staunton chess set is preferred.

The Chess Set: The Chess Set is a 2005 Australian short subject depicting two old men Stuart Wagstaff and Frank Wilson who enjoy their daily chess game in a park.  One day a young stranger (Nathaniel Dean) joins them to watch their game, leaving his blood on one of the men.  Grief soon follows, but turns to hope.

MIK (character set): MIK (МИК) is a 8-bit Cyrillic code page used with DOS.  It is based on the character set used in the Bulgarian Pravetz 16 IBM PC compatible system.  Kermit calls this character set "BULGARIA-PC" / "bulgaria-pc".  In Bulgaria, it was sometimes incorrectly referred to as code page 856 (which clashes with IBM's definition for a Hebrew code page).

Question: The offical chess set used in competions is named after who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "chess_set_name": {
      "type": "string",
      "description": "The name of the chess set style."
    },
    "named_after_person": {
      "type": "string",
      "description": "The person after whom the chess set is named."
    },
    "competition_use": {
      "type": "boolean",
      "description": "Indicates if the chess set style is required for competitions."
    },
    "designer_credited": {
      "type": "string",
      "description": "The person credited with the design of the chess set."
    },
    "first_available_year": {
      "type": "integer",
      "description": "The year the chess set style was first made available."
    }
  },
  "required": [
    "chess_set_name",
    "named_after_person",
    "competition_use",
    "designer_credited",
    "first_available_year"
  ],
  "additionalProperties": false
}

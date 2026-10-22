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
Creamy Mami, the Magic Angel: Creamy Mami, the Magic Angel (魔法の天使クリィミーマミ , Mahō no Tenshi Kurīmī Mami ) is a magical girl anime series by Studio Pierrot which aired from 1983 to 1984 on Nippon Television.  It went on to have five OVA adaptions and featured in other Studio Pierrot special presentations.  A three volume manga was released during the original TV run, with the story written by Kazunori Itō and art by Yuuko Kitagawa.  This was the first of five magical girl anime to be produced by Studio Pierrot, and the first of these to feature the designs of Akemi Takada.  In 2005, the web-poll for TV Asahi's top-100 anime of all time saw "Creamy Mami, the Magic Angel" poll 82nd.  The series is currently streaming in North America via Yomiuri TV's Anime Sols video service, as of spring 2013.  Thus far, a limited DVD release of all 52 TV episodes has been successfully crowd-funded at Anime Sols.  Leftover copies of the first boxset are currently up at Right Stuf and Crunchyroll.

Rita (TV series): Rita is a Danish comedy-drama TV series on TV 2.  It premiered in February 2012 and has run for three seasons in Denmark and internationally on Netflix which was also a co-producer on the third and fourth season.

Video over LTE: ViLTE, an acronym for Video over LTE, is a conversational (i.e. person to person) video service based on the IP Multimedia Subsystem (IMS) core network.  It has specific profiles for the control and media planes of the video service and uses LTE as the radio access medium.  The service as a whole is governed by the GSM Association in PRD IR.94.

Sadik Mikhou: Sadik Mikhou (born 25 July 1990) is a Moroccan-born middle-distance runner who since 2015 runs internationally for Bahrain.  He competed at the 2017 World Championships finishing sixth.  Additionally, he won the gold at the 2017 Islamic Solidarity Games.  He swit

Candy Boy: Candy☆Boy (キャンディ ボーイ , Kyandi Bōi ) is an eight-minute original net animation produced by Anime International Company, and directed by Takafumi Hoshikawa.  Since November 22, 2007, the ONA is available through streaming on the Cho!  animelo audiovisual website and the Nico Nico Douga online video service.  This was followed by a seven-episode series, with episodes being streamed between May 2, 2008 and May 8, 2009.  Additional episodes were released on DVD, one with the DVD version of the single, "Bring Up Love" by Nayuta, and another released with volume 2 of the series.  A spin-off manga series by Hiro Tōge was serialized in Media Factory's Comic Flapper magazine between November 2009 and December 2010, with another series, also by Tōge, distributed on mobile phones.

Microsoft Movies &amp; TV: Movies & TV (Canada and the US), or Films & TV (UK, Ireland, Australia, and New Zealand), previously Xbox Video and Zune Video, is a digital video service developed by Microsoft that offers full HD movies and TV shows available for rental or purchase in the "Video Store".  The service is available on Xbox 360, Xbox One, Windows 8 and later, and Windows Phone 8 and later.  Movies & TV is also accessible on the web.

Hjørdis (TV series): Hjørdis is a spin-off of the Danish TV series Rita.  It follows school teacher Hjørdis as she tries to put together a school play about bullying.

Dundee Channel: The Dundee Channel is an internet video service based in Dundee Scotland which streams both live and pre-recorded videos with news and features from Tayside, Angus, Perth and Fife.  Having begun life in 1999 as a video documentary service it moved on line in 2009.  It was an early adopter of the Livestream technology allowing video pictures to be sent via the internet.  As of 2014 it is now using wifi technology to webcast video via mobile devices primarily using Apple technology.

Thomson Video Networks: Thomson Video Networks is a technology broadcast company that provides video compression, transcoding and processing solutions for media companies, video service providers, and TV broadcasters.  The firm has offices in 16 countries and headquarters in Rennes, France.

OnCue: OnCue was an online pay-TV service developed by Intel.  In December 2013, Intel sought to sell the OnCue service.  Verizon purchased the service for $200 million.  Verizon repurposed the service for its Go90 internet video service.  The Go90 service is estimated to launch in late July or early August 2015.

Question: Hjørdis is a spin-off of a TV Danish series that runs internationally on what video service?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "spin_off_series_name": {
      "type": "string",
      "description": "The name of the spin-off TV series."
    },
    "original_series_name": {
      "type": "string",
      "description": "The name of the original TV series from which the spin-off originated."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the original TV series was produced."
    },
    "international_streaming_service": {
      "type": "string",
      "description": "The video service on which the original series runs internationally."
    }
  },
  "required": [
    "spin_off_series_name",
    "original_series_name",
    "country_of_origin",
    "international_streaming_service"
  ],
  "additionalProperties": false
}

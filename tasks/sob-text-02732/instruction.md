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
Virtual Boy: The Virtual Boy is a 32-bit table-top video game console developed and manufactured by Nintendo.  Released in 1995, it was marketed as the first console capable of displaying stereoscopic 3D graphics.  Virtual Boy is also the first video game system ever to display in widescreen; it would be 14 years until another system would be widescreen again.  The player uses the console in a manner similar to a head-mounted display, placing their head against the eyepiece to see a red monochrome display.  The games use a parallax effect to create the illusion of depth.  Sales failed to meet targets, and by early 1996, Nintendo ceased distribution and game development, only ever releasing 22 games for the system.

VR HMD mount: A virtual reality head-mounted display (VR HMD) mount is a mount for attaching a VR head-mounted display.  It is distinct from a virtual reality headset, like the Oculus Rift, HTC Vive, Sony Morpheus, Carl Zeiss VR One, as a VR HMD mount does not contain any electronics or screen itself, but rather allows users to insert a smartphone or other device in it and place it on the head.

The Sword of Damocles (virtual reality): The Sword of Damocles is widely considered to be the first virtual reality (VR) head-mounted display (HMD) system.  It was created in 1968 by computer scientist Ivan Sutherland with the help of his student Bob Sproull.  Before he began working toward what he termed "the ultimate display", Ivan Sutherland was already well respected for his accomplishments in computer graphics (see Sketchpad).  At MIT's Lincoln Laboratory beginning in 1966, Sutherland and his colleagues performed what is widely believed to be the first experiments with head-mounted displays of different kinds.

Virtual reality headset: A virtual reality headset is a head-mounted device that provides virtual reality for the wearer.  VR headsets are widely used with computer games but they are also used in other applications, including simulators and trainers.  They comprise a stereoscopic head-mounted display (providing separate images for each eye), stereo sound, and head motion tracking sensors (which may include gyroscopes, accelerometers, structured light systems, etc.).  Some VR headsets also have eye tracking sensors and gaming controllers.

VirtuSphere: VirtuSphere is a virtual reality device.  It is, as the name suggests, spherical.  It consists of a 10-foot hollow sphere, which is placed on a special platform that allows the sphere to rotate freely in any direction according to the user’s steps.  It works with computer based simulations and virtual worlds, and rotates as the user walks, allowing for an unlimited plane upon which the user can walk.  A wireless head-mounted display with gyroscopes is used to both track the user's head movement as well as display the environment of the virtual world.  VirtuSphere can serve many purposes, including exercise, video gaming, military training, and virtual museum tours.

PlayStation VR: The PlayStation VR, known by the codename Project Morpheus during development, is a virtual reality headset developed by Sony Interactive Entertainment, which was released in October 2016.

Robinson: The Journey: Robinson: The Journey is a first-person shooter virtual reality video game developed and published by Crytek.  The game released for the PlayStation 4 in November 2016, and for Microsoft Windows in February 2017.  The game uses the PlayStation VR and Oculus Rift virtual reality headsets respectively on each platform.

Palmer Luckey: Palmer Freeman Luckey (born September 19, 1992) is an American entrepreneur.  He is the founder of Oculus VR and designer of the Oculus Rift, a virtual reality head-mounted display.  Luckey ranks #22 on Forbes' 2016 list of America's richest entrepreneurs under 40.

Virtual Reality Website: A Virtual Reality Website is a website that leverages the WebVR and WebGL APIs to create a 3D environment for a web user to explore using a virtual reality head-mounted display.

RIGS: Mechanized Combat League: RIGS: Mechanized Combat League is a first-person shooter sports video game developed by Guerrilla Cambridge and published by Sony Interactive Entertainment for the PlayStation 4 console and its virtual reality head-mounted display PlayStation VR.

Question: Who developed a first-person shooter sports video game for the PlayStation 4 console and its virtual reality head-mounted display  known by the codename Project Morpheus during development?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_title": {
      "type": "string",
      "description": "The title of the video game."
    },
    "game_genre": {
      "type": "string",
      "description": "The genre of the video game."
    },
    "developer": {
      "type": "string",
      "description": "The developer of the video game."
    },
    "platform": {
      "type": "string",
      "description": "The primary console platform for the game."
    },
    "vr_headset_used": {
      "type": "string",
      "description": "The virtual reality headset used with the game."
    },
    "vr_headset_codename": {
      "type": "string",
      "description": "The codename of the virtual reality headset during development."
    }
  },
  "required": [
    "game_title",
    "game_genre",
    "developer",
    "platform",
    "vr_headset_used",
    "vr_headset_codename"
  ],
  "additionalProperties": false
}

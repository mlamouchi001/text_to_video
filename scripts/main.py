from text_analysis import analyze_text
from text_analysis import split_text_by_actions
from image_generation import generate_anime_image
from voice_generation import generate_voice
from video_creation import create_video
import os


def main():
    text = (
        "In the year 3025, the world had changed beyond recognition. Skyscrapers soared high above the clouds, vehicles hovered in the sky, and robots walked side by side with humans, forming a delicate balance of cohabitation. Technology had advanced to a point where almost anything was possible. The cities were illuminated by neon lights, and artificial intelligence was woven into the fabric of everyday life. However, with these advancements came new dangers—malfunctioning robots, rogue AI systems, and cybernetic creatures that had gone awry. "
        "At the center of this world, in a state-of-the-art facility nestled in the heart of Neonopolis, Professor Zivor was hard at work. Zivor was a visionary scientist, known throughout the city for his work in cybernetics and artificial intelligence. Yet, despite his impressive achievements, Zivor remained a humble, kind-hearted man, motivated not by fame or wealth, but by a desire to protect the people of Neonopolis from the technological threats that emerged as the city's systems grew ever more complex. "
        "For years, Zivor had been working on a special project, one that combined his love of animals with his passion for technology. His goal was to create a protector for the city—a guardian that could navigate the dense urban environment, fast, agile, and capable of fighting off any robotic threats that surfaced. But this protector needed more than just brute strength. It needed intelligence, curiosity, and above all, adaptability. That’s when the idea came to him: a cybernetic cat. "
        "On a quiet evening in the lab, after years of trials, calculations, and countless hours of coding, the project was finally complete. As Zivor activated the final sequence, sparks flew from the wires, and a soft hum filled the room. On the large steel table in front of him, a small cat-shaped figure began to stir. Its sleek, metallic body glinted under the fluorescent lights. Its eyes, glowing a soft blue, blinked for the first time. And then, with a twitch of its tail and a stretch of its mechanical legs, the creature rose to its feet. "
        "“Hello, little one,” Zivor said softly, kneeling down beside the table to meet the creature’s gaze. The cat looked up at him, head tilting slightly in curiosity. A moment passed before it made a sound—a soft, mechanical purr that brought a smile to Zivor’s face. "
        "Paws was born. "
        "But Paws wasn’t an ordinary cat. Beneath his metallic fur lay a powerful array of cybernetic enhancements. His **advanced AI** allowed him to think and learn like a living creature, adapting to new environments and situations. His **laser claws** could cut through metal and dismantle rogue robots in seconds, making him the perfect defense against any mechanical threat. His **tail**, far from being just a decorative feature, could extend, acting as a grappling hook, a tool for hacking systems, or even a whip in combat. All of these abilities were designed with one purpose in mind: to protect Neonopolis. "
        "However, despite all of his enhancements, Paws was more than just a machine. Zivor had infused him with a sense of curiosity, playfulness, and a desire to explore. Paws was, after all, still a cat. His movements, sleek and fluid, were reminiscent of the felines of old. He could leap gracefully across rooftops, climb walls with ease, and sneak through even the narrowest spaces without making a sound. "
        "For days, Paws explored the lab, testing his newfound abilities under Zivor’s watchful eye. He practiced using his claws, slashing through holographic enemies that Zivor projected into the room. He learned to activate his tail's various functions, using it to latch onto walls and pull himself to higher vantage points. And though his combat skills were formidable, it was Paws’ intellect that impressed Zivor the most. The little cyber-cat was not only fast and strong, but he also learned from every situation, storing information and analyzing data at lightning speed. "
        "One day, while Paws was lounging in a sunbeam that filtered through the lab’s windows, Zivor approached him with a thoughtful look on his face. \"I think it’s time,\" the professor said, scratching behind Paws’ metallic ears, eliciting another soft purr. \"You’re ready to see the world outside.\" "
        "Paws perked up at this. He had heard the sounds of the city beyond the lab—distant, mechanical whirs, the hum of engines, and the occasional screech of metal against metal. The outside world was a place of mystery to him, and his AI-driven curiosity made him eager to explore it. "
        "With a series of soft beeps, the doors to the lab slid open, revealing the vast expanse of Neonopolis for the first time. The city stretched as far as the eye could see, a jungle of towering skyscrapers bathed in the glow of neon signs and holographic advertisements. Flying cars zipped through the sky on invisible highways, while drones and robots bustled through the streets below, attending to their daily routines. "
        "Paws’ sensors came alive as he stepped out into this new world. He could feel the electromagnetic pulses of the city’s systems, the hum of energy coursing through the streets, and the distant chatter of the city's inhabitants. Every sound, every movement was a new data point to be analyzed. But more than anything, Paws was fascinated. His blue eyes widened as he took in the sights, his tail flicking in excitement. "
        "Zivor, standing behind him, smiled. “This is your new home, Paws,” he said. “Out there is where you’ll make a difference.” "
        "But Neonopolis wasn’t just a beautiful, futuristic city. It was also filled with danger. Rogue AI systems had been known to take over robotic systems, turning them against the humans they were designed to serve. Recently, a group of robotic drones had gone rogue, attacking the city’s power grid. The city’s authorities had been struggling to control the situation, and that was why Zivor had created Paws—to be the first line of defense against these threats. "
        "For now, though, the city seemed calm. Paws’ sensors detected no immediate threats, and his AI prompted him to explore. With a burst of speed, he dashed down the streets, weaving between pedestrians and robots alike. The people of Neonopolis barely noticed the small metallic cat running among them, just another piece of high-tech machinery in a city full of it. "
        "As Paws continued his exploration, he began to realize that the city held more secrets than he could have imagined. There were hidden alleyways, rooftop hideouts, and abandoned factories where rogue robots lurked in the shadows. His AI processed every new piece of information, mapping the city in intricate detail, preparing him for the challenges ahead. "
        "But Paws wasn’t just a machine following pre-programmed commands. He was curious. He stopped to observe the world around him—the way humans interacted with their technology, the patterns of the flying cars, the rhythm of the city itself. And even though he was a cyber-cat, he couldn’t resist the urge to chase the occasional stray light reflection or laser pointer. After all, some things never change. "
        "As night fell over Neonopolis, the city came alive with a different kind of energy. Neon lights flickered on, casting a vibrant glow over the streets. Paws found himself perched on the edge of a rooftop, looking out over the skyline. The distant hum of engines and the chatter of the city's inhabitants filled the air. "
        "For the first time in his short existence, Paws felt a sense of purpose. He had been created to protect this city, to defend it from the dangers lurking in the shadows. But more than that, he wanted to explore, to understand, and to learn. And so, with the neon lights of the city reflecting in his glowing blue eyes, Paws made a silent vow. He would protect Neonopolis, not because it was his duty, but because it was his home. "
        "This was only the beginning of his journey."
    )

    # Analyse du texte
    ##scenes = analyze_text(text)
    scenes = split_text_by_actions(text)

    print(len(scenes))

    image_paths = []
    audio_path = "audio/narration.mp3"

    # Génération des images pour chaque scène en style manga
    for i, scene in enumerate(scenes):
        image_path = f"images/scene_{i}.png"
        generate_anime_image(scene, image_path)
        image_paths.append(image_path)

    # Génération de la narration vocale
    generate_voice(text, audio_path)

    # Création de la vidéo animée
    create_video(image_paths, audio_path, "video/final_anime_video.mp4")


if __name__ == "__main__":
    main()

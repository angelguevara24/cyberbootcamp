# Make the My_House folder
mkdir My_House

# Change into the My_House folder
cd My_House

# Make the room folders
mkdir Bedroom Living_Room Kitchen

# Change into the Living_Room
cd Living_Room

# Create the TV and Sofa
touch tv.txt sofa.txt

# Change into the Kitchen
cd ..
cd Kitchen

# Create the Oven and Sink
touch oven.txt
touch sink.txt

# Return to the bedroom
cd ..

# Create the bedroom items
touch bed.txt

# Create the bathroom in the bedroom
mkdir Bathroom

# Return to the Kitchen and copy the sink to the Bathroom
cd ..
cd Kitchen
cp sink.txt ../Bedroom/Bathroom

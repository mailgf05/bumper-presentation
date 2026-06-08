#!/bin/bash

# Presentation Validation Script
echo "🔍 Validating Bumper Mission Book Presentation..."
echo ""

# Check if HTML file exists
if [ -f "bumper-presentation.html" ]; then
    echo "✅ HTML file exists"
    SIZE=$(du -h bumper-presentation.html | cut -f1)
    echo "   Size: $SIZE"
else
    echo "❌ HTML file missing"
    exit 1
fi

# Check if image data exists
if [ -f "image_data.json" ]; then
    echo "✅ Image data file exists"
    IMG_SIZE=$(du -h image_data.json | cut -f1)
    echo "   Size: $IMG_SIZE"
else
    echo "⚠️  Image data file missing (images may not load)"
fi

# Check README
if [ -f "README.md" ]; then
    echo "✅ README documentation exists"
else
    echo "⚠️  README missing"
fi

# Check launcher
if [ -x "start-presentation.sh" ]; then
    echo "✅ Launcher script is executable"
else
    echo "⚠️  Launcher script not executable"
fi

# Count slides in HTML
SLIDES=$(grep -c '<div class="slide' bumper-presentation.html || echo "0")
echo "📊 Found $SLIDES slides in presentation"

# Check for key sections
echo ""
echo "📋 Checking content sections:"

for section in "Mission" "SWOT" "Personas" "Concurrentielle" "Bumper Lab" "Réseaux Sociaux" "Calendrier" "Objectifs SMART" "Conclusion"; do
    if grep -q "$section" bumper-presentation.html; then
        echo "✅ $section section found"
    else
        echo "❌ $section section missing"
    fi
done

echo ""
echo "🎨 Design elements check:"
if grep -q "#00C9AF" bumper-presentation.html; then
    echo "✅ Bumper brand colors present"
fi
if grep -q "Google Fonts" bumper-presentation.html; then
    echo "✅ Google Fonts linked"
fi
if grep -q "Font Awesome" bumper-presentation.html; then
    echo "✅ Font Awesome icons loaded"
fi

echo ""
echo "🚀 Presentation is ready to view!"
echo "   Run: ./start-presentation.sh"
echo "   Or open: bumper-presentation.html"
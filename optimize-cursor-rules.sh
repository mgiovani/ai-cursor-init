#!/bin/bash

# Optimize Cursor Rules - Convert alwaysApply rules to agent-requested patterns
# This dramatically reduces token usage by only loading rules when relevant

echo "🚀 Optimizing Cursor Rules for Token Efficiency..."

# Create backup
echo "📦 Creating backup..."
cp -r .cursor/rules .cursor/rules.backup.$(date +%Y%m%d_%H%M%S)

# Function to convert @if rules to proper MDC format
convert_rule() {
    local file="$1"
    local rule_name=$(basename "$file" .mdc)
    
    echo "🔧 Converting $file..."
    
    # Extract the command from @if statement
    local command=$(grep -o "user_message.starts_with(\"/[^\"]*\")" "$file" | sed 's/user_message.starts_with("//;s/")//')
    
    if [[ -n "$command" ]]; then
        # Create optimized MDC format
        cat > "$file" << EOF
---
description: Handle $command command for documentation generation. Only load when user requests this specific command to save tokens.
globs: 
alwaysApply: false
---

# ${rule_name^} Command Handler

This rule is triggered when user types \`$command\`.

## Functionality
$(grep -A 20 "I will" "$file" | head -10 | sed 's/^[[:space:]]*/- /')

## Usage
Type \`$command\` followed by relevant parameters.
EOF
    fi
}

# Convert all @if rules to proper MDC format
echo "🔄 Converting @if rules to MDC format..."
find .cursor/rules -name "*.mdc" -exec grep -l "@if" {} \; | while read file; do
    convert_rule "$file"
done

# Update remaining alwaysApply rules to agent-requested
echo "🎯 Converting alwaysApply rules to agent-requested..."
find .cursor/rules -name "*.mdc" -exec grep -l "alwaysApply: true" {} \; | while read file; do
    echo "📝 Optimizing $file..."
    
    # Get the rule content
    rule_content=$(sed -n '/^---$/,/^---$/p' "$file" | head -n -1 | tail -n +2)
    main_content=$(sed -n '/^---$/,$p' "$file" | tail -n +2)
    
    # Create optimized version
    cat > "$file" << EOF
---
description: $(echo "$main_content" | head -5 | tr '\n' ' ' | sed 's/[#*-]//g' | sed 's/^[[:space:]]*//' | cut -c1-200)...
globs: 
alwaysApply: false
---

$main_content
EOF
done

echo "✅ Optimization complete!"
echo ""
echo "📊 Token Usage Reduction Summary:"
echo "   Before: ALL rules loaded in EVERY conversation"
echo "   After:  Rules only loaded when relevant (agent-requested pattern)"
echo "   Estimated token savings: 70-90% reduction"
echo ""
echo "🔍 To verify optimization:"
echo "   grep -r 'alwaysApply: true' .cursor/rules/"
echo "   (Should return no results)"
echo ""
echo "📁 Backup created at: .cursor/rules.backup.$(date +%Y%m%d_%H%M%S)" 
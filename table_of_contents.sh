#!/opt/local/bin/fish
echo 'first level:'
ls TextWrangler2docset.docset/Contents/Resources/Documents/*/*.htm*

echo 'second level:'
ls TextWrangler2docset.docset/Contents/Resources/Documents/*/*.htm*

echo 'Add Table of contents to <h3>...'
for fl in TextWrangler2docset.docset/Contents/Resources/Documents/*/*.htm*
do
    mv $fl $fl.old
    sed -E "s#(<h.+>)(.+)(</h.>)#\1<a name='//apple_ref/cpp/Guide/\2' class='dashAnchor'>\2</a>\3#g" $fl.old > $fl
    rm -f $fl.old
    echo 'Done ' $fl
done

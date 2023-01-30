package abstract_factory;

import builder_pattern.MazeBuilder;

public class client {
    public static void main(String[] args) {

        // IN that case, we must have at least two product class
        // here product class are Window and ScrollBar
        // WidgetFactory widgetFactory = new MotifWidgetFactory();

        // widgetFactory.CreateScrollBar();
        // widgetFactory.CreateWindow();

        WidgetMaker widgetMaker = new WidgetMaker();
        widgetMaker.createWidget(new PMWIdgetFactory());
        // * that's the use case where certain factory is passed where each factory 
        // * resembles different implementation of scrollbar, window etc.
    }
}
